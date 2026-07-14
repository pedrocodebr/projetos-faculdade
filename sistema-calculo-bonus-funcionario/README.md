# 📌 Sistema de Cálculo de Bônus de Funcionários

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula uma aplicação de Recursos Humanos (RH) responsável por calcular automaticamente o bônus de um funcionário com base no seu salário e na avaliação de desempenho recebida.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como entrada e saída de dados, operações matemáticas e estruturas condicionais, desenvolvendo uma solução capaz de aplicar regras de negócio para definir bonificações de funcionários.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita o salário do funcionário;
- Solicita a avaliação de desempenho:
  - **Excelente**
  - **Boa**
  - **Regular**
- Analisa os critérios definidos para cada avaliação;
- Calcula o valor do bônus correspondente;
- Exibe o valor final do bônus recebido.

Regras aplicadas:

- Funcionário com avaliação **excelente**:
  - Recebe **20% de bônus** sobre o salário.

- Funcionário com avaliação **boa**:
  - Salário abaixo de R$ 5.000,00 recebe **10% de bônus**;
  - Salário igual ou superior a R$ 5.000,00 recebe **5% de bônus**.

- Funcionário com avaliação **regular**:
  - Salário abaixo de R$ 3.000,00 recebe **5% de bônus**;
  - Salário igual ou superior a R$ 3.000,00 não recebe bônus.

- Caso a avaliação informada seja inválida, o sistema informa o erro.

## ✨ Funcionalidades

- Cálculo automático de bônus;
- Aplicação de regras de avaliação de desempenho;
- Validação da categoria informada pelo usuário;
- Exibição do valor do bônus formatado em reais.

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
- Operadores relacionais;
- Operadores aritméticos;
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
📁 sistema-calculo-bonus-funcionario
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o aprimoramento da lógica de programação, permitindo aplicar estruturas condicionais na criação de regras de negócio semelhantes às utilizadas em sistemas empresariais. A prática ajudou a compreender como diferentes critérios podem influenciar automaticamente o resultado de uma operação.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos iniciais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**. Apesar da simplicidade, demonstra a criação de uma solução automatizada para processos relacionados à área de Recursos Humanos.

Como evolução futura, o sistema poderá ser ampliado com cadastro de funcionários, armazenamento de dados, geração de relatórios, integração com banco de dados e criação de uma interface gráfica.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**