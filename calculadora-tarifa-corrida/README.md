# 📌 Calculadora de Tarifa de Corrida

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula o cálculo do valor de uma corrida com base na distância percorrida, no horário da viagem e na aplicação de descontos conforme regras previamente definidas.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python para desenvolver um sistema capaz de calcular automaticamente o valor de uma corrida. Durante sua implementação foram utilizados operadores aritméticos, estruturas condicionais e entrada de dados para representar uma situação prática do cotidiano.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita a distância percorrida em quilômetros;
- Solicita a hora em que a corrida foi realizada;
- Define automaticamente o valor cobrado por quilômetro:
  - **Das 22h às 5h59:** tarifa de R$ 3,50 por quilômetro;
  - **Das 6h às 21h59:** tarifa de R$ 2,50 por quilômetro.
- Calcula o valor total da corrida;
- Caso a distância percorrida seja superior a **20 km**, aplica automaticamente um desconto de **10%**;
- Exibe o valor final da corrida.

## ✨ Funcionalidades

- Cálculo automático da tarifa da corrida;
- Alteração da tarifa conforme o horário informado;
- Aplicação automática de desconto para corridas acima de 20 km;
- Exibição do valor final formatado em reais.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis
- Entrada e saída de dados
- Conversão de tipos (`int` e `float`)
- Operadores aritméticos
- Operadores relacionais
- Operadores lógicos (`or`)
- Estruturas condicionais (`if` e `else`)
- Formatação de saída utilizando *f-strings*

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 calculadora-tarifa-corrida
├── main.py
└── README.md
```

## 📚 Aprendizados

Este projeto permitiu aplicar conceitos importantes de lógica de programação, especialmente na construção de regras condicionais para diferentes cenários. Além disso, reforçou o uso de operadores lógicos, cálculos matemáticos e organização do fluxo de execução de um programa.

## 💭 Considerações Finais

Este projeto representa mais uma aplicação prática desenvolvida durante minha formação em **Análise e Desenvolvimento de Sistemas**. A implementação demonstra como a programação pode ser utilizada para automatizar cálculos baseados em regras de negócio. Como evolução futura, o sistema poderá incluir diferentes categorias de veículos, tarifas dinâmicas, cadastro de corridas e emissão de comprovantes.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**
