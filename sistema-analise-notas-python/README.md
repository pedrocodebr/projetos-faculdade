# 📌 Sistema de Análise de Notas de Alunos

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema permite registrar notas de alunos, realizar validações dos valores informados e gerar uma análise com base na média das notas cadastradas.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos de listas, estruturas de repetição, validação de informações e processamento de dados, desenvolvendo uma solução capaz de armazenar notas e gerar informações úteis a partir dos resultados obtidos.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita notas ao usuário;
- Permite encerrar o cadastro digitando o valor **-1**;
- Valida se a nota está dentro do intervalo permitido;
- Armazena apenas notas válidas;
- Calcula a média geral das notas;
- Verifica quantas notas ficaram acima da média;
- Exibe os resultados da análise.

Regras aplicadas:

- Notas entre **0 e 10**:
  - São consideradas válidas e armazenadas.

- Notas menores que 0 ou maiores que 10:
  - São rejeitadas pelo sistema.

- Valor **-1**:
  - Encerra o cadastro de notas.

## ✨ Funcionalidades

- Cadastro de múltiplas notas;
- Validação automática dos valores;
- Armazenamento das notas em uma lista;
- Cálculo da média da turma;
- Identificação de alunos acima da média;
- Geração de resumo dos resultados.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Listas;
- Entrada e saída de dados;
- Conversão de tipos (`float`);
- Estruturas de repetição:
  - `while`
  - `for`
- Estruturas condicionais:
  - `if`
  - `else`
- Controle de fluxo:
  - `break`
  - `continue`
- Métodos de listas:
  - `.append()`
- Funções nativas:
  - `sum()`
  - `len()`
- Variáveis acumuladoras;
- Contadores;
- Validação de dados;
- Análise de informações.

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 sistema-analise-notas-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o aprimoramento da lógica de programação, permitindo compreender como sistemas podem coletar informações, validar dados e gerar análises automaticamente.

A utilização de listas possibilitou trabalhar com uma quantidade variável de registros, aproximando o projeto de aplicações reais utilizadas para controle acadêmico e gerenciamento de informações.

## 💭 Considerações Finais

Este projeto representa uma evolução nos estudos de programação em Python durante minha formação em **Análise e Desenvolvimento de Sistemas**.

Comparado aos primeiros exercícios, este sistema apresenta uma estrutura mais próxima de uma aplicação real, pois realiza entrada de dados, armazenamento, processamento e geração de resultados.

Como evolução futura, o projeto poderá ser expandido com:
- Cadastro de nomes dos alunos;
- Associação entre aluno e nota;
- Geração de boletins;
- Armazenamento em arquivos;
- Banco de dados;
- Organização utilizando funções e programação orientada a objetos.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**