# 📌 Sistema de Análise de Média Salarial

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema permite registrar salários informados pelo usuário e calcula automaticamente a média dos valores válidos cadastrados.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos de estruturas de repetição, validação de dados e variáveis acumuladoras, desenvolvendo uma solução capaz de coletar informações financeiras e gerar uma análise dos dados registrados.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita salários ao usuário;
- Valida os valores informados;
- Ignora entradas iguais a zero;
- Encerra o cadastro quando um valor negativo é informado;
- Soma todos os salários válidos;
- Conta a quantidade de registros realizados;
- Calcula a média salarial.

Regras aplicadas:

- Salário maior que **0**:
  - É considerado válido e utilizado no cálculo.

- Salário igual a **0**:
  - É ignorado pelo sistema.

- Salário menor que **0**:
  - Encerra a entrada de dados.

## ✨ Funcionalidades

- Cadastro contínuo de salários;
- Validação de valores;
- Cálculo automático da média salarial;
- Contagem de registros válidos;
- Tratamento de ausência de dados;
- Processamento de informações financeiras.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Conversão de tipos (`float`);
- Estruturas de repetição:
  - `while`
- Estruturas condicionais:
  - `if`
  - `else`
- Controle de fluxo:
  - `break`
  - `continue`
- Variáveis acumuladoras;
- Contadores;
- Cálculo de média;
- Validação de dados;
- Processamento de informações.

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 media-salarial-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o entendimento de como sistemas podem coletar dados financeiros, validar informações e gerar resultados automaticamente.

A utilização de acumuladores e contadores permitiu praticar uma lógica semelhante à utilizada em relatórios e análises de dados.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**.

Apesar de sua simplicidade, demonstra uma estrutura semelhante a sistemas administrativos, onde informações são coletadas, processadas e transformadas em indicadores.

Como evolução futura, o projeto poderá ser expandido com:

- Cadastro de funcionários;
- Associação entre nome e salário;
- Cálculo de maior e menor salário;
- Geração de relatórios;
- Armazenamento em arquivos;
- Integração com banco de dados;
- Organização utilizando funções e orientação a objetos.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**