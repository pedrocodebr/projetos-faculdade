# 📌 Sistema de Classificação de Prioridade de Atendimento

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula uma classificação de prioridade de atendimento, utilizando informações como idade do usuário e gravidade dos sintomas para definir diferentes níveis de prioridade.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como entrada e saída de dados, operadores lógicos e estruturas condicionais, desenvolvendo uma solução capaz de analisar informações e retornar uma classificação automaticamente com base em regras definidas.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita a idade do usuário;
- Solicita a gravidade dos sintomas:
  - **Leve**
  - **Moderada**
  - **Grave**
- Analisa as condições informadas;
- Define a prioridade de atendimento conforme as regras estabelecidas;
- Exibe uma mensagem com a classificação resultante.

Regras aplicadas:

- Sintomas **graves**:
  - Atendimento imediato.

- Sintomas **moderados**:
  - Usuários acima de 60 anos recebem prioridade;
  - Demais usuários aguardam atendimento normal.

- Sintomas **leves**:
  - Usuários menores de 12 anos ou maiores de 65 anos recebem prioridade moderada;
  - Demais usuários aguardam atendimento comum.

- Caso a opção informada seja inválida:
  - O sistema informa erro de entrada.

## ✨ Funcionalidades

- Classificação automática de prioridade;
- Análise de idade e gravidade dos sintomas;
- Validação das informações inseridas;
- Aplicação de regras de decisão;
- Exibição do resultado do atendimento.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Conversão de tipos (`int`);
- Manipulação de strings:
  - `.strip()`
  - `.lower()`
- Estruturas condicionais (`if`, `elif` e `else`);
- Operadores relacionais;
- Operadores lógicos:
  - `or`
- Regras de negócio;
- Tomada de decisão baseada em critérios.

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 sistema-triagem-atendimento-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o fortalecimento da lógica de programação, permitindo aplicar estruturas condicionais e operadores lógicos na criação de sistemas baseados em regras. A implementação simulou um cenário de tomada de decisão, demonstrando como programas podem analisar diferentes informações e retornar resultados automaticamente.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos iniciais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**. Apesar de ser uma simulação simples, demonstra a utilização de lógica condicional para resolver problemas envolvendo classificação e prioridade.

Como evolução futura, o projeto poderá ser expandido com cadastro de pacientes, armazenamento de histórico de atendimentos, integração com banco de dados e criação de uma interface gráfica.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**
