"""
gerar_readme_ollama.py

Gera README.md automaticamente para cada projeto dentro de uma pasta raiz,
usando um modelo de IA rodando LOCALMENTE via Ollama (100% gratuito, sem
limite de requisições, sem precisar de internet depois de baixar o modelo).
"""

import os
import re
import requests

# ============ CONFIGURAÇÕES (AJUSTE AQUI) ============

DIRETORIO_RAIZ = r"C:\Users\pedro\OneDrive\Área de Trabalho\VS CODE FACULDADE"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5-coder:7b"

EXTENSOES_CODIGO = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".cs",
    ".html", ".css", ".ipynb", ".sql", ".php", ".rb", ".go"
}

IGNORAR_PASTAS = {".git", "node_modules", "__pycache__", "venv", ".venv", "dist", "build", ".idea"}

LIMITE_CARACTERES_CODIGO = 15000

# =======================================================


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


def gerar_readme(nome_projeto, codigo):
    prompt = f"""Você é um assistente que documenta projetos de programação para o GitHub.

Analise o código abaixo do projeto "{nome_projeto}" e gere um README.md profissional em português com estas seções, nesta ordem:

# {nome_projeto}

## Descrição
(o que o projeto faz, de forma clara)

## Objetivo
(qual era a intenção ao criar este projeto)

## O que foi praticado/aprendido
(conceitos técnicos, lógica de programação, bibliotecas usadas)

## Tecnologias utilizadas
(liste as linguagens/bibliotecas identificadas no código)

## Como executar
(passos simples para rodar o projeto)

Código do projeto:
{codigo}

Responda APENAS com o conteúdo do README.md em markdown puro. Não escreva nenhum comentário fora do markdown, não use blocos de código ```markdown envolvendo tudo."""

    return perguntar_ollama(prompt)


def sugerir_nome_pasta(nome_arquivo, codigo):
    prompt = f"""Sugira um nome de pasta curto e descritivo (em minúsculas, palavras separadas por hífen,
formato "nome-do-projeto", sem espaços, sem acentos) para um projeto Python cujo arquivo se chama
"{nome_arquivo}" e tem este código:

{codigo[:3000]}

Responda APENAS com o nome da pasta, nada mais. Exemplo de resposta válida: calculadora-de-notas"""

    resposta = perguntar_ollama(prompt).strip().splitlines()[0]
    nome_limpo = re.sub(r"[^a-z0-9\-]", "", resposta.lower().replace(" ", "-"))
    return nome_limpo or "projeto-sem-nome"


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
            nome_pasta = sugerir_nome_pasta(nome_arquivo, codigo)

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

    proc_pastas, ignoradas = processar_pastas_existentes()
    proc_soltos = processar_arquivos_soltos()

    print("\n🏁 Concluído!")
    print(f"   - {proc_pastas} README(s) gerados em pastas existentes")
    print(f"   - {ignoradas} pasta(s) ignoradas (já tinham README)")
    print(f"   - {proc_soltos} arquivo(s) solto(s) organizados em novas pastas")