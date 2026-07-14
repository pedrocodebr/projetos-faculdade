# Gerador Automático de README com IA

Ferramenta em Python que analisa projetos de código e gera automaticamente uma documentação (`README.md`) para cada um, usando um modelo de linguagem rodando localmente via [Ollama](https://ollama.com).

## 📌 Sobre o Projeto

Durante a faculdade, acumulei dezenas de pequenos projetos em Python e precisava de um jeito rápido de documentar cada um deles sem escrever manualmente um README para cada pasta. Esse script resolve isso: ele lê o código de cada projeto, entende o que ele faz e gera automaticamente:

- Um **nome de pasta** mais descritivo, baseado no que o código realmente faz
- Um **README.md completo**, com descrição do projeto, tecnologias usadas e instruções de execução

## 🤖 Como Funciona

Para cada pasta de projeto encontrada:

1. **Verifica se já existe um `README.md`** — se já existir, a pasta é ignorada por completo (nada é alterado).
2. **Lê todos os arquivos `.py`** dentro da pasta e junta o conteúdo.
3. **Envia o código para o modelo local (llama3, via Ollama)**, pedindo um nome de pasta curto e descritivo em kebab-case (ex: `calculadora-de-imc-python`).
4. **Renomeia a pasta** para o nome sugerido (só se não houver conflito com uma pasta já existente).
5. **Pede ao modelo um README completo** descrevendo o projeto, e salva como `README.md` dentro da pasta (já com o nome de pasta atualizado).
6. Ao final, **atualiza o README raiz** do repositório com a lista de todos os projetos processados.

## 🛠️ Tecnologias

- Python
- [Ollama](https://ollama.com) (modelo `llama3` rodando localmente)
- Biblioteca `requests`

## 🚀 Como Executar

**1. Pré-requisitos:**

```bash
pip install requests
ollama pull llama3
```

O Ollama precisa estar rodando em segundo plano (na maioria das instalações no Windows ele já inicia sozinho; se não, rode `ollama serve` em outro terminal).

**2. Posicionamento:**

Coloque o arquivo `gerar_readme.py` na pasta raiz que contém os projetos que você quer documentar (ele usa a própria localização como ponto de partida).

**3. Execução:**

```bash
python gerar_readme.py
```

O script vai processar cada subpasta, uma por vez, mostrando no terminal o que está fazendo em cada etapa.

## ⚠️ Observações

- Pastas que já têm `README.md` **não são tocadas** — nem o conteúdo, nem o nome da pasta.
- Pastas sem nenhum arquivo `.py` são ignoradas.
- Se o Ollama não estiver rodando, o script avisa e para, em vez de travar com um erro.
- As pastas `sistema_readme` e `python-project-generator` (usadas pelo próprio bot) são ignoradas automaticamente.

## 👤 Autor

**Pedro Leonardo Piancó Tenório**