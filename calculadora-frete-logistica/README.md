# 📌 Sistema de Cálculo de Frete

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula uma aplicação de cálculo de frete, determinando o custo de entrega de uma encomenda com base no peso do produto e na distância de transporte.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como entrada e saída de dados, estruturas condicionais e operações matemáticas, desenvolvendo uma solução capaz de calcular automaticamente valores de entrega utilizando regras de negócio.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita o peso da encomenda em quilogramas;
- Solicita a distância da entrega em quilômetros;
- Verifica se a encomenda está dentro do limite permitido para transporte;
- Calcula o valor inicial do frete de acordo com o peso;
- Adiciona uma taxa extra caso a distância ultrapasse o limite definido;
- Exibe o custo final da entrega.

Regras aplicadas:

- Encomendas acima de **50 kg**:
  - Não podem ser transportadas.

- Encomendas até **5 kg**:
  - Custo base de R$ 10,00.

- Encomendas entre **5 kg e 20 kg**:
  - Custo base de R$ 20,00.

- Encomendas acima de **20 kg até 50 kg**:
  - Custo base de R$ 40,00.

- Entregas com distância superior a **50 km**:
  - Acréscimo de R$ 15,00 no valor final.

## ✨ Funcionalidades

- Cálculo automático do valor do frete;
- Validação do limite máximo de peso;
- Aplicação de taxas adicionais por distância;
- Classificação da encomenda conforme peso;
- Exibição do custo final formatado em reais.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Conversão de tipos (`float`);
- Estruturas condicionais (`if`, `elif` e `else`);
- Estruturas condicionais aninhadas;
- Operadores relacionais;
- Operadores aritméticos;
- Atualização de valores com operadores de atribuição (`+=`);
- Regras de negócio;
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
📁 sistema-calculo-frete-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o aprimoramento da lógica de programação, permitindo aplicar estruturas condicionais na criação de sistemas baseados em regras comerciais.

A implementação simulou um cenário encontrado em plataformas de comércio eletrônico e logística, onde diferentes características de um produto influenciam diretamente no cálculo de valores.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos iniciais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**. Mesmo sendo uma aplicação simples, demonstra a criação de um sistema automatizado para cálculo de valores utilizando diferentes critérios.

Como evolução futura, o projeto poderá ser expandido com cadastro de produtos, cálculo de múltiplas encomendas, integração com banco de dados, criação de histórico de entregas e desenvolvimento de uma interface gráfica.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**
