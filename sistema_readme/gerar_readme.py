"""
gerar_readme_ollama_v3.py

Gera README.md profissional para cada projeto dentro de uma pasta raiz,
usando um modelo de IA rodando LOCALMENTE via Ollama (100% gratuito, sem
limite de requisições).

Novidades desta versão:
  - Corrige acentos ao gerar nomes de pasta (ex: "números" agora vira
    corretamente "numeros", não "nmeros").
  - Gera/atualiza um README.md na RAIZ do repositório, com um índice
    listando todos os projetos e um link para cada um.
"""

import os
import re
import unicodedata
import requests

# ============ CONFIGURAÇÕES (AJUSTE AQUI) ============

DIRETORIO_RAIZ = r"C:\Users\pedro\OneDrive\Área de Trabalho\VS CODE FACULDADE"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5-coder:7b"

AUTOR_NOME = "Pedro Leonardo Piancó Tenório"
CURSO = "Análise e Desenvolvimento de Sistemas (ADS)"

# Link do repositório no GitHub (usado para montar os links no README raiz)
GITHUB_REPO_URL = "https://github.com/pedrocodebr/projetos-faculdade"

EXTENSOES_CODIGO = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".cs",
    ".html", ".css", ".ipynb", ".sql", ".php", ".rb", ".go"
}

IGNORAR_PASTAS = {".git", "node_modules", "__pycache__", "venv", ".venv", "dist", "build", ".idea"}

LIMITE_CARACTERES_CODIGO = 15000

PADRAO_NOME_GENERICO = re.compile(r"^(att?|atividade|projeto)[\s\-]?\d*(-python|\s*faculdade)?$", re.IGNORECASE)

# =======================================================


def remover_acentos(texto):
    """Remove acentos preservando a letra base (ex: 'número' -> 'numero')."""
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def slugificar(texto):
    """Converte texto em um slug seguro para nome de pasta (minúsculo, hífens, sem acentos)."""
    texto = remover_acentos(texto)
    texto = texto.lower().strip()
    texto = re.sub(r"[^a-z0-9\-\s]", "", texto)
    texto = re.sub(r"[\s_]+", "-", texto)
    texto = re.sub(r"-+", "-", texto).strip("-")
    return texto


def ler_codigo_projeto(caminho_pasta):
    conteudo = ""
    for raiz, pastas, arquivos in os.walk(caminho_pasta):
        pastas[:] = [p for p in pastas if p not in IGNORAR_PASTAS]
        for arquivo in arquivos:
            ext = os.path.splitext(arquivo)[1].lower()
            if ext in EXTENSOES_CODIGO:
                caminho_completo = os.path.join(raiz, arquivo)
                try:
                    with open(caminho_completo, "r", encoding="utf-8", errors="ignore") as f:
                        texto = f.read()
                    conteudo += f"\n\n### Arquivo: {arquivo}\n{texto}"
                except Exception as e:
                    print(f"    Aviso: não consegui ler '{arquivo}' ({e})")
    return conteudo[:LIMITE_CARACTERES_CODIGO]


def perguntar_ollama(prompt):
    resposta = requests.post(
        OLLAMA_URL,
        json={"model": MODELO, "prompt": prompt, "stream": False},
        timeout=600,
    )
    resposta.raise_for_status()
    return resposta.json()["response"].strip()


def sugerir_nome_pasta(codigo, nome_atual):
    prompt = f"""Sugira um nome de pasta curto e descritivo (em minúsculas, palavras separadas por hífen,
formato "nome-do-projeto-python", sem espaços, pode ter acentos que serão removidos depois) para um
projeto Python que atualmente se chama "{nome_atual}" e tem este código:

{codigo[:3000]}

Responda APENAS com o nome da pasta, nada mais, sem explicações. Exemplo de resposta válida: sistema-media-escolar-python"""

    resposta = perguntar_ollama(prompt).strip().splitlines()[0]
    nome_limpo = slugificar(resposta)
    return nome_limpo or None


def renomear_pastas_genericas():
    itens = os.listdir(DIRETORIO_RAIZ)
    candidatas = [
        i for i in itens
        if os.path.isdir(os.path.join(DIRETORIO_RAIZ, i))
        and i not in IGNORAR_PASTAS
        and PADRAO_NOME_GENERICO.match(i.strip())
    ]

    if not candidatas:
        print("ℹ️  Nenhuma pasta com nome genérico encontrada para renomear.\n")
        return {}

    print(f"🏷️  {len(candidatas)} pasta(s) com nome genérico encontrada(s). Renomeando...\n")

    mapa_renomeacao = {}

    for nome_atual in candidatas:
        caminho_atual = os.path.join(DIRETORIO_RAIZ, nome_atual)
        codigo = ler_codigo_projeto(caminho_atual)

        if not codigo.strip():
            print(f"⚠️  '{nome_atual}' está vazia ou sem código reconhecido — mantendo nome.")
            continue

        print(f"🤖 Analisando '{nome_atual}' para sugerir novo nome...")
        try:
            novo_nome = sugerir_nome_pasta(codigo, nome_atual)
            if not novo_nome:
                print(f"⚠️  Não consegui gerar nome para '{nome_atual}' — mantendo original.")
                continue

            sufixo = 1
            novo_nome_final = novo_nome
            while os.path.exists(os.path.join(DIRETORIO_RAIZ, novo_nome_final)):
                sufixo += 1
                novo_nome_final = f"{novo_nome}-{sufixo}"

            caminho_novo = os.path.join(DIRETORIO_RAIZ, novo_nome_final)
            os.rename(caminho_atual, caminho_novo)
            mapa_renomeacao[nome_atual] = novo_nome_final
            print(f"✅ '{nome_atual}' renomeada para '{novo_nome_final}'\n")
        except requests.exceptions.ConnectionError:
            print("❌ Não consegui conectar ao Ollama. Ele está rodando? (ollama serve)")
            break
        except Exception as e:
            print(f"❌ Erro ao renomear '{nome_atual}': {e}\n")

    return mapa_renomeacao


def gerar_readme(nome_projeto, codigo):
    prompt = f"""Você é um assistente que documenta projetos de programação em português, no estilo de um
portfólio acadêmico de estudante de {CURSO}.

Gere um README.md profissional e completo para o projeto "{nome_projeto}", seguindo EXATAMENTE esta
estrutura de seções (mantenha os emojis e os títulos como estão):

# 📌 [Nome do projeto em formato de título, condizente com o que o código faz]

## 📖 Descrição
(contexto: projeto feito durante estudos de programação, curso {CURSO}. Explique o que o sistema faz.)

## 🎯 Objetivo
(quais conceitos de programação o projeto teve como objetivo praticar)

## 📝 Sobre o Projeto
(passo a passo do que o programa faz, em bullet points. Se fizer sentido, inclua um exemplo de entrada e saída.)

## ✨ Funcionalidades
(lista em bullet points das funcionalidades do sistema)

## 🛠️ Tecnologias Utilizadas
(linguagens e bibliotecas identificadas no código)

## 🧠 Conceitos Praticados
(lista técnica: estruturas de dados, laços, funções, bibliotecas específicas, etc, identificados no código real)

## ▶️ Como Executar
(passos numerados para rodar o projeto, incluindo o comando `python nome_do_arquivo.py`)

## 📂 Estrutura do Projeto
(bloco de código mostrando a árvore de arquivos da pasta, baseado nos arquivos reais mencionados no código fornecido)

## 📚 Aprendizados
(parágrafo sobre o que a prática deste projeto agregou ao aprendizado)

## 💭 Considerações Finais
(parágrafo de fechamento, mencionando possíveis evoluções futuras do projeto)

## 👨‍💻 Autor

**{AUTOR_NOME}**

---

Código do projeto (analise para extrair nomes de arquivos, bibliotecas e lógica real, não invente funcionalidades que não existem no código):
{codigo}

Responda APENAS com o conteúdo do README.md em markdown puro, sem comentários fora do markdown, sem envolver tudo em blocos ```markdown."""

    return perguntar_ollama(prompt)


def extrair_descricao_curta(caminho_readme):
    """Pega a primeira frase da seção 'Descrição' de um README já gerado, para usar no índice raiz."""
    try:
        with open(caminho_readme, "r", encoding="utf-8") as f:
            conteudo = f.read()
        match = re.search(r"##\s*📖?\s*Descri[cç][aã]o\s*\n+(.+)", conteudo)
        if match:
            frase = match.group(1).strip().split("\n")[0]
            frase = re.sub(r"[*_`]", "", frase)
            return frase[:150]
    except Exception:
        pass
    return ""


def gerar_readme_raiz():
    """Gera/atualiza o README.md da raiz do repositório com um índice de todos os projetos."""
    itens = sorted(os.listdir(DIRETORIO_RAIZ))
    pastas = [
        i for i in itens
        if os.path.isdir(os.path.join(DIRETORIO_RAIZ, i)) and i not in IGNORAR_PASTAS
    ]

    linhas = [
        "# Projetos da Faculdade",
        "",
        f"Este repositório reúne os projetos e exercícios desenvolvidos durante minha graduação em **{CURSO}**.",
        "",
        "Cada pasta contém um projeto independente, com seu próprio README explicando a descrição, objetivo, "
        "conceitos praticados e como executar.",
        "",
        "## 📂 Projetos",
        "",
    ]

    for nome_pasta in pastas:
        caminho_readme_projeto = os.path.join(DIRETORIO_RAIZ, nome_pasta, "README.md")
        link = f"{GITHUB_REPO_URL}/tree/main/{nome_pasta}" if GITHUB_REPO_URL else nome_pasta

        if os.path.exists(caminho_readme_projeto):
            descricao = extrair_descricao_curta(caminho_readme_projeto)
            if descricao:
                linhas.append(f"- **[{nome_pasta}]({link})** — {descricao}")
            else:
                linhas.append(f"- **[{nome_pasta}]({link})**")
        else:
            linhas.append(f"- **[{nome_pasta}]({link})** — _(sem README ainda)_")

    linhas += [
        "",
        "## 🛠️ Tecnologias",
        "",
        "- Python",
        "",
        "## 👨‍💻 Autor",
        "",
        f"**{AUTOR_NOME}**",
        "",
    ]

    caminho_readme_raiz = os.path.join(DIRETORIO_RAIZ, "README.md")
    with open(caminho_readme_raiz, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print(f"✅ README.md da raiz atualizado com {len(pastas)} projeto(s) listado(s).\n")


def processar_pastas_existentes():
    itens = os.listdir(DIRETORIO_RAIZ)
    pastas = [
        i for i in itens
        if os.path.isdir(os.path.join(DIRETORIO_RAIZ, i)) and i not in IGNORAR_PASTAS
    ]

    print(f"📁 {len(pastas)} pastas encontradas para verificar.\n")

    processados, ignorados = 0, 0

    for nome_pasta in pastas:
        caminho_pasta = os.path.join(DIRETORIO_RAIZ, nome_pasta)
        caminho_readme = os.path.join(caminho_pasta, "README.md")

        if os.path.exists(caminho_readme):
            print(f"⏭️  '{nome_pasta}' já tem README.md — pulando.")
            ignorados += 1
            continue

        codigo = ler_codigo_projeto(caminho_pasta)
        if not codigo.strip():
            print(f"⚠️  '{nome_pasta}' não tem arquivos de código reconhecidos — pulando.")
            continue

        print(f"🤖 Gerando README para '{nome_pasta}'...")
        try:
            texto_readme = gerar_readme(nome_pasta, codigo)
            with open(caminho_readme, "w", encoding="utf-8") as f:
                f.write(texto_readme)
            print(f"✅ README.md criado em '{nome_pasta}'\n")
            processados += 1
        except requests.exceptions.ConnectionError:
            print("❌ Não consegui conectar ao Ollama. Ele está rodando? (ollama serve)")
            return processados, ignorados
        except Exception as e:
            print(f"❌ Erro ao processar '{nome_pasta}': {e}\n")

    return processados, ignorados


def processar_arquivos_soltos():
    itens = os.listdir(DIRETORIO_RAIZ)
    arquivos_soltos = [
        i for i in itens
        if os.path.isfile(os.path.join(DIRETORIO_RAIZ, i)) and os.path.splitext(i)[1].lower() in EXTENSOES_CODIGO
    ]

    if not arquivos_soltos:
        return 0

    print(f"\n📄 {len(arquivos_soltos)} arquivo(s) solto(s) encontrado(s) na raiz.\n")
    processados = 0

    for nome_arquivo in arquivos_soltos:
        caminho_arquivo = os.path.join(DIRETORIO_RAIZ, nome_arquivo)
        try:
            with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
                codigo = f.read()
        except Exception as e:
            print(f"❌ Não consegui ler '{nome_arquivo}': {e}")
            continue

        print(f"🤖 Organizando '{nome_arquivo}'...")
        try:
            nome_pasta = sugerir_nome_pasta(codigo, nome_arquivo) or "projeto-sem-nome"

            sufixo = 1
            nome_pasta_final = nome_pasta
            while os.path.exists(os.path.join(DIRETORIO_RAIZ, nome_pasta_final)):
                sufixo += 1
                nome_pasta_final = f"{nome_pasta}-{sufixo}"
            caminho_nova_pasta = os.path.join(DIRETORIO_RAIZ, nome_pasta_final)

            os.makedirs(caminho_nova_pasta)
            os.replace(caminho_arquivo, os.path.join(caminho_nova_pasta, nome_arquivo))

            texto_readme = gerar_readme(nome_pasta_final, codigo[:LIMITE_CARACTERES_CODIGO])
            with open(os.path.join(caminho_nova_pasta, "README.md"), "w", encoding="utf-8") as f:
                f.write(texto_readme)

            print(f"✅ Movido para pasta '{nome_pasta_final}' com README.md\n")
            processados += 1
        except Exception as e:
            print(f"❌ Erro ao organizar '{nome_arquivo}': {e}\n")

    return processados


if __name__ == "__main__":
    print("=== Organizador automático de projetos com IA local (Ollama) ===\n")

    if not os.path.isdir(DIRETORIO_RAIZ):
        print(f"❌ Pasta não encontrada: {DIRETORIO_RAIZ}")
        print("   Ajuste a variável DIRETORIO_RAIZ no início do script.")
        exit(1)

    print("--- Etapa 1: Renomeando pastas com nomes genéricos ---\n")
    renomear_pastas_genericas()

    print("--- Etapa 2: Gerando READMEs dos projetos ---\n")
    proc_pastas, ignoradas = processar_pastas_existentes()
    proc_soltos = processar_arquivos_soltos()

    print("--- Etapa 3: Atualizando README raiz (índice de projetos) ---\n")
    gerar_readme_raiz()

    print("\n🏁 Concluído!")
    print(f"   - {proc_pastas} README(s) gerados em pastas existentes")
    print(f"   - {ignoradas} pasta(s) ignoradas (já tinham README)")
    print(f"   - {proc_soltos} arquivo(s) solto(s) organizados em novas pastas")
    print("   - README.md da raiz atualizado com índice de todos os projetos")