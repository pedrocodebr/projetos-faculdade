"""
gerar_readme.py

Varre as pastas de projetos Python dentro do diretório onde este script está,
usa o Ollama (modelo local) para:
  1. Sugerir um novo nome de pasta baseado no que o código faz
  2. Gerar um README.md completo para o projeto

Requisitos:
  - Ollama instalado e rodando (https://ollama.com)
  - Modelo baixado: ollama pull llama3
  - Biblioteca requests: pip install requests

Uso:
  Coloque este arquivo na raiz da pasta que contém os projetos e rode:
    python gerar_readme.py
"""

import os
import re
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"
AUTOR = "Pedro Leonardo Piancó Tenório"
CURSO = "Análise e Desenvolvimento de Sistemas"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Pastas que o script nunca deve tocar
IGNORE_DIRS = {
    ".git", ".vscode", "__pycache__",
    "sistema_readme", "python-project-generator",
}


def get_python_files_content(folder_path):
    """Concatena o conteúdo de todos os .py dentro da pasta do projeto."""
    content = ""
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content += f"\n# Arquivo: {file}\n" + f.read()
                except Exception as e:
                    print(f"   ⚠️  Erro ao ler {file_path}: {e}")
    return content.strip()


def call_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Não consegui conectar ao Ollama. Confirme que ele está rodando "
            "(abra outro terminal e rode: ollama serve) e que o modelo foi baixado "
            f"(ollama pull {MODEL})."
        )


def suggest_folder_name(code_content, current_name):
    prompt = f"""Analise o código Python abaixo e sugira um nome de pasta curto e descritivo,
em português, usando apenas letras minúsculas, números e hífens (kebab-case),
terminando com "-python". Responda APENAS com o nome sugerido, sem explicações,
sem aspas e sem pontuação extra.

Nome atual da pasta: {current_name}

Código:
{code_content[:3000]}
"""
    result = call_ollama(prompt)
    slug = result.strip().splitlines()[0] if result else ""
    slug = re.sub(r"[^a-z0-9\-]", "", slug.lower().replace(" ", "-"))
    return slug or current_name


def generate_readme(code_content, project_name):
    prompt = f"""Você é um assistente que gera documentação README.md para projetos Python
de faculdade. Com base no código abaixo, gere um README.md completo em português,
em Markdown, contendo:
- Título com o nome do projeto
- Uma breve descrição do que o programa faz
- Seção "Tecnologias" (Python)
- Seção "Como Executar" com instruções básicas
- Seção "Autor" com o nome: {AUTOR}

Nome do projeto: {project_name}

Código:
{code_content[:3000]}

Responda apenas com o conteúdo do README.md em Markdown, sem comentários extras.
"""
    return call_ollama(prompt)


def process_project(folder_path):
    folder_name = os.path.basename(folder_path)
    readme_path = os.path.join(folder_path, "README.md")

    if os.path.exists(readme_path):
        print(f"⏭️  '{folder_name}' já tem README.md — pulando.")
        return folder_path

    code_content = get_python_files_content(folder_path)
    if not code_content:
        print(f"⚠️  '{folder_name}' não tem arquivos .py — pulando.")
        return folder_path

    print(f"🤖 Analisando '{folder_name}'...")

    new_name = suggest_folder_name(code_content, folder_name)
    new_path = folder_path
    if new_name and new_name != folder_name:
        candidate_path = os.path.join(os.path.dirname(folder_path), new_name)
        if not os.path.exists(candidate_path):
            os.rename(folder_path, candidate_path)
            new_path = candidate_path
            print(f"✏️  Renomeado: '{folder_name}' → '{new_name}'")
        else:
            print(f"⚠️  Já existe uma pasta '{new_name}', mantendo nome original.")

    readme_content = generate_readme(code_content, os.path.basename(new_path))
    with open(os.path.join(new_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"✅ README.md criado em '{os.path.basename(new_path)}'.")
    return new_path


def update_root_readme(root_dir, project_folders):
    lines = [
        "# Projetos da Faculdade\n",
        f"Este repositório reúne os projetos e exercícios desenvolvidos durante minha "
        f"graduação em **{CURSO}**.\n",
        "Cada pasta contém um projeto independente, com seu próprio README explicando "
        "a descrição, objetivo, conceitos praticados e como executar.\n",
        "## 📁 Projetos\n",
    ]
    for folder in sorted(project_folders):
        lines.append(f"- [{folder}]({folder})")
    lines.append("\n## 🛠️ Tecnologias\n")
    lines.append("- Python\n")
    lines.append("## 👤 Autor\n")
    lines.append(f"**{AUTOR}**\n")

    with open(os.path.join(root_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\n✅ README.md da raiz atualizado com {len(project_folders)} projeto(s) listado(s).")


def main():
    project_folders = []
    for item in sorted(os.listdir(ROOT_DIR)):
        item_path = os.path.join(ROOT_DIR, item)
        if os.path.isdir(item_path) and item not in IGNORE_DIRS and not item.startswith("."):
            try:
                final_path = process_project(item_path)
            except RuntimeError as e:
                print(f"❌ {e}")
                return
            project_folders.append(os.path.basename(final_path))

    update_root_readme(ROOT_DIR, project_folders)
    print("🏁 Concluído!")


if __name__ == "__main__":
    main()