# 📌 Sistema de Análise de Bolsa de Estudos

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula uma análise de elegibilidade para concessão de bolsa de estudos, utilizando critérios como renda familiar mensal e desempenho acadêmico do aluno.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como entrada e saída de dados, operadores lógicos e estruturas condicionais, desenvolvendo uma solução capaz de analisar diferentes critérios e determinar automaticamente se um aluno atende aos requisitos para receber uma bolsa de estudos.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita a renda familiar mensal do aluno;
- Solicita a média das notas obtidas;
- Analisa os critérios de elegibilidade;
- Compara os valores informados com as regras definidas;
- Exibe o resultado da análise.

Critérios utilizados:

- Média **maior ou igual a 9,0** e renda familiar **até R$ 5.000,00**:
  - Aluno elegível para bolsa.

- Média **maior ou igual a 8,0** e renda familiar **menor que R$ 3.000,00**:
  - Aluno elegível para bolsa.

- Média entre **7,0 e 7,9** e renda familiar **menor que R$ 2.000,00**:
  - Aluno elegível para bolsa.

- Caso nenhum critério seja atendido:
  - Aluno não elegível para bolsa.

## ✨ Funcionalidades

- Análise automática de critérios de bolsa;
- Avaliação baseada em desempenho acadêmico;
- Verificação da renda familiar;
- Aplicação de múltiplas regras de decisão;
- Exibição do resultado final da análise.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Conversão de tipos (`float`);
- Estruturas condicionais (`if`, `elif` e `else`);
- Operadores relacionais;
- Operadores lógicos:
  - `and`
- Comparações em intervalos;
- Criação de regras de negócio;
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
📁 sistema-analise-bolsa-estudos-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o aprimoramento da lógica de programação, permitindo aplicar operadores lógicos e estruturas condicionais na criação de sistemas baseados em regras. A prática ajudou a compreender como diferentes critérios podem ser combinados para gerar decisões automáticas.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos iniciais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**. Mesmo sendo uma simulação simples, demonstra a criação de um sistema capaz de analisar informações e tomar decisões utilizando critérios previamente definidos.

Como evolução futura, o projeto poderá ser expandido com cadastro de alunos, armazenamento de informações, geração de relatórios, integração com banco de dados e criação de uma interface gráfica.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**