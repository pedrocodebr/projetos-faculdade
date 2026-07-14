# 📌 Sistema de Análise de Compras

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema permite registrar valores de compras, calcular automaticamente a média das compras realizadas e identificar quantas delas ficaram acima da média.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como listas, estruturas de repetição, estruturas condicionais e validação de dados, por meio da implementação de um sistema capaz de armazenar informações e gerar estatísticas simples.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita o valor de cada compra;
- Armazena apenas compras válidas em uma lista;
- Ignora valores iguais a zero;
- Encerra o cadastro quando um valor negativo é informado;
- Calcula a média das compras registradas;
- Conta quantas compras possuem valor acima da média;
- Exibe um resumo com os resultados obtidos.

### Regras aplicadas

- **Valor maior que R$ 0,00:**
  - É armazenado para análise.

- **Valor igual a R$ 0,00:**
  - É ignorado.

- **Valor negativo:**
  - Finaliza o cadastro das compras.

## ✨ Funcionalidades

- Cadastro contínuo de compras;
- Armazenamento de valores em lista;
- Validação automática das entradas;
- Cálculo da média das compras;
- Contagem de compras acima da média;
- Exibição de resumo estatístico.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis
- Listas (`list`)
- Entrada e saída de dados
- Conversão de tipos (`float`)
- Estruturas de repetição (`while` e `for`)
- Estruturas condicionais (`if` e `else`)
- Controle de fluxo (`break` e `continue`)
- Método de listas (`append`)
- Funções nativas (`sum()` e `len()`)
- Cálculo de média
- Comparação de valores
- Formatação de saída com *f-strings*

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 analise-compras-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o fortalecimento da lógica de programação, permitindo aplicar conceitos de armazenamento de dados em listas, processamento de informações e cálculo de indicadores estatísticos simples.

Além disso, possibilitou praticar a validação de entradas e a utilização de estruturas de repetição para análise de dados.

## 💭 Considerações Finais

Este projeto representa uma evolução dos estudos em Python durante minha formação em **Análise e Desenvolvimento de Sistemas**. Embora seja um sistema simples, demonstra a utilização de listas para armazenamento de dados e o processamento de informações para obtenção de estatísticas, técnicas amplamente utilizadas em aplicações comerciais e sistemas de gestão.

Como melhoria futura, o sistema poderá ser expandido para permitir o cadastro de produtos, geração de relatórios, cálculo do valor total das vendas, identificação da maior e da menor compra, além da utilização de funções para modularização do código.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**