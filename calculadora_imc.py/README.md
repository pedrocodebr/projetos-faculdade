# 📌 Sistema de Classificação de IMC

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema realiza o cálculo do Índice de Massa Corporal (IMC) de diversos usuários e classifica os resultados em diferentes categorias.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos de estruturas de repetição, validação de dados, cálculos matemáticos e classificação de informações, desenvolvendo uma solução capaz de processar dados de entrada e gerar uma análise automática.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita o peso do usuário;
- Solicita a altura informada;
- Calcula o IMC utilizando os valores recebidos;
- Classifica o resultado em categorias;
- Contabiliza a quantidade de pessoas em cada categoria;
- Exibe um resumo final da análise.

Classificações utilizadas:

- **Abaixo do peso:**
  - IMC menor que 18,5.

- **Peso normal:**
  - IMC entre 18,5 e menor que 25.

- **Acima do peso:**
  - IMC igual ou superior a 25.

Regras aplicadas:

- Peso negativo:
  - Encerra o cadastro.

- Altura menor ou igual a zero:
  - Entrada inválida, sendo ignorada.

## ✨ Funcionalidades

- Cadastro contínuo de informações;
- Cálculo automático do IMC;
- Classificação dos resultados;
- Contagem por categoria;
- Validação de entradas;
- Geração de resumo final.

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
  - `elif`
  - `else`
- Operadores matemáticos;
- Cálculo de porcentagem e índices;
- Variáveis contadoras;
- Controle de fluxo:
  - `break`
  - `continue`
- Classificação de dados;
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
📁 classificador-imc-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o aprendizado de como sistemas podem receber dados, realizar cálculos e classificar informações automaticamente.

A utilização de contadores permitiu criar um resumo dos resultados obtidos, uma lógica semelhante à utilizada em sistemas de relatórios e análise de dados.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**.

Apesar de ser um projeto simples, apresenta uma estrutura próxima de sistemas reais que precisam coletar informações, aplicar regras e gerar classificações.

Como evolução futura, o projeto poderá ser expandido com:

- Cadastro de usuários;
- Armazenamento dos dados;
- Histórico de avaliações;
- Geração de relatórios;
- Interface gráfica;
- Banco de dados;
- Organização utilizando funções e orientação a objetos.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**