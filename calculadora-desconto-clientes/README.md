# 📌 Sistema de Cálculo de Desconto para Clientes

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula uma aplicação de vendas capaz de calcular automaticamente o desconto de uma compra com base na categoria do cliente e no valor total da compra.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como entrada e saída de dados, operadores matemáticos e estruturas condicionais, desenvolvendo uma solução capaz de aplicar regras de negócio para calcular o valor final de uma compra.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita o valor total da compra;
- Solicita a categoria do cliente:
  - **Premium**
  - **Comum**
- Analisa as regras de desconto de acordo com a categoria e valor da compra;
- Calcula automaticamente o desconto aplicado;
- Exibe o valor final da compra após o desconto.

Regras aplicadas:

- Cliente **Premium**:
  - Compras acima de R$ 500,00 recebem **20% de desconto**;
  - Compras até R$ 500,00 recebem **10% de desconto**.

- Cliente **Comum**:
  - Compras acima de R$ 500,00 recebem **10% de desconto**;
  - Compras até R$ 500,00 não recebem desconto.

## ✨ Funcionalidades

- Cálculo automático de descontos;
- Diferenciação entre categorias de clientes;
- Aplicação de regras comerciais;
- Exibição do valor final da compra formatado em reais.

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
- Operadores aritméticos;
- Operadores relacionais;
- Cálculo percentual;
- Formatação de saída com *f-strings*.

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 sistema-calculo-desconto-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para a evolução da lógica de programação, permitindo aplicar estruturas condicionais na criação de regras de negócio. A implementação simulou um cenário próximo ao encontrado em sistemas comerciais, onde diferentes condições influenciam o resultado final de uma operação.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos iniciais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**. Apesar de sua simplicidade, demonstra a capacidade de criar sistemas que automatizam processos e aplicam decisões baseadas em diferentes critérios.

Como evolução futura, o projeto poderá receber melhorias como cadastro de clientes, histórico de compras, integração com banco de dados e criação de uma interface gráfica para utilização.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**
