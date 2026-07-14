# 📌 Sistema de Validação de Saque Bancário

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula uma operação de saque bancário, realizando validações de saldo disponível, valor solicitado e necessidade de confirmação adicional para operações acima de um limite definido.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como entrada e saída de dados, operadores lógicos e estruturas condicionais, desenvolvendo uma solução capaz de validar operações financeiras com base em regras previamente estabelecidas.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita o saldo disponível na conta;
- Solicita o valor do saque desejado;
- Verifica se o cliente possui saldo suficiente;
- Valida se o valor informado é permitido;
- Analisa saques acima do limite estabelecido;
- Solicita confirmação adicional quando necessário;
- Exibe o resultado da operação.

Regras aplicadas:

- Caso o valor do saque seja maior que o saldo disponível:
  - Operação negada por falta de saldo.

- Caso o valor do saque seja menor ou igual a zero:
  - Operação inválida.

- Caso o saque seja superior a R$ 1.000,00:
  - É necessária uma confirmação adicional.

- Caso nenhuma regra de bloqueio seja aplicada:
  - O saque é realizado com sucesso.

## ✨ Funcionalidades

- Validação de saldo disponível;
- Verificação de valores inválidos;
- Controle de limite de saque;
- Confirmação adicional para operações de maior valor;
- Exibição do resultado da transação.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Conversão de tipos (`float`);
- Manipulação de strings:
  - `.strip()`
  - `.lower()`
- Estruturas condicionais (`if`, `elif` e `else`);
- Estruturas condicionais aninhadas;
- Operadores relacionais;
- Operadores lógicos;
- Validação de regras de negócio;
- Simulação de fluxo de aprovação.

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 sistema-validacao-saque-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o fortalecimento da lógica de programação, permitindo aplicar estruturas condicionais simples e aninhadas para criar um fluxo de validação semelhante ao utilizado em sistemas reais.

A prática ajudou a compreender como diferentes condições podem influenciar uma operação e como regras de negócio são transformadas em lógica computacional.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos iniciais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**. Apesar de ser uma simulação simplificada, demonstra a criação de um sistema capaz de analisar informações, aplicar restrições e controlar uma operação financeira.

Como evolução futura, o sistema poderá ser expandido com autenticação de usuário, histórico de transações, cadastro de contas, armazenamento de dados em banco de dados e integração com uma interface gráfica.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**
