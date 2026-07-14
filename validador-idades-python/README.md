# 📌 Sistema de Validação e Análise de Idades

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema realiza o cadastro de idades informadas pelo usuário, aplicando validações para garantir que apenas valores dentro do intervalo permitido sejam considerados no cálculo da média.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos de validação de dados, estruturas de repetição e variáveis acumuladoras, desenvolvendo uma solução capaz de receber informações, verificar sua validade e gerar uma análise com base nos dados registrados.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita idades ao usuário continuamente;
- Permite encerrar a entrada digitando o valor **0**;
- Verifica se a idade informada está dentro do intervalo permitido;
- Ignora valores inválidos;
- Armazena a soma das idades válidas;
- Conta a quantidade de registros aceitos;
- Calcula e exibe a média das idades cadastradas.

Regras aplicadas:

- Idades entre **10 e 100 anos**:
  - São consideradas válidas e adicionadas ao cálculo.

- Idades menores que 10 ou maiores que 100:
  - São rejeitadas pelo sistema.

- Valor **0**:
  - Encerra o cadastro e inicia a análise dos dados.

## ✨ Funcionalidades

- Entrada contínua de dados;
- Validação automática de idades;
- Tratamento de informações inválidas;
- Cálculo da média das idades válidas;
- Controle da quantidade de registros;
- Encerramento personalizado do sistema.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Conversão de tipos (`int`);
- Estruturas de repetição:
  - `while`
- Controle de fluxo:
  - `break`
  - `continue`
- Estruturas condicionais:
  - `if`
  - `else`
- Operadores lógicos:
  - `or`
- Variáveis acumuladoras;
- Contadores;
- Validação de dados;
- Cálculo de média;
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
📁 validador-idades-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o aprimoramento da lógica de programação, permitindo compreender como sistemas podem validar informações antes de realizar operações com os dados recebidos.

A prática reforçou conceitos importantes como tratamento de entradas inválidas, controle de repetição e processamento de informações coletadas durante a execução.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**.

Mesmo sendo um sistema simples, demonstra uma estrutura semelhante a aplicações reais que precisam receber dados de usuários, validar informações e gerar resultados automaticamente.

Como evolução futura, o projeto poderá ser expandido para armazenar as idades em listas, gerar relatórios estatísticos, criar gráficos, utilizar funções e integrar armazenamento em banco de dados.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**