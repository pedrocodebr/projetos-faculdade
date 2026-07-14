# gerador-readme-ollama

## Descrição
O projeto "gerador-readme-ollama" é uma ferramenta que automatiza a geração de README.md profissionais para projetos de programação localmente utilizando o modelo de linguagem IA Ollama. A ferramenta lê o código dos arquivos dentro de uma pasta raiz, cria um README em português com seções específicas e sugere um nome de pasta descritivo para projetos soltos.

## Objetivo
O objetivo deste projeto é facilitar a documentação do desenvolvimento de software, permitindo que programadores criem READMEs consistentes e profissionais sem precisar fazer isso manualmente.

## O que foi praticado/aprendido
Este projeto serviu como um bom exercício para aplicar conceitos de programação orientada a objetos, lógica de negócios, manipulação de arquivos e comunicação com APIs. Também aprendemos sobre o uso de modelos linguísticos IA localmente e como integrá-los em uma aplicação Python.

## Tecnologias utilizadas
- Python 3.x
- Requests (biblioteca para chamadas HTTP)
- Ollama API

## Como executar
1. Clone ou baixe o repositório do GitHub.
2. Configure a variável `DIRETORIO_RAIZ` no arquivo `gerador_readme_ollama.py` com o caminho da pasta raiz que contém seus projetos.
3. Certifique-se de ter o Ollama API rodando localmente na porta 11434 (pode ser necessário ajustar a URL e o modelo conforme necessário).
4. Execute o script `gerador_readme_ollama.py` em seu ambiente Python.

```bash
python gerador_readme_ollama.py
```

O script percorrerá a pasta raiz especificada, lendo os arquivos de código, chamando a API do Ollama para gerar um README.md profissional e organizando projetos soltos em pastas descritivas.