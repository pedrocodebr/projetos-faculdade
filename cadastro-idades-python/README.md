# 📌 Sistema de Análise de Idades

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema permite registrar idades informadas pelo usuário, validar os dados de entrada e calcular automaticamente a média das idades válidas.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos de estruturas de repetição, validação de dados e cálculo de médias, desenvolvendo uma solução capaz de processar informações de forma segura e gerar indicadores estatísticos simples.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita a idade do usuário;
- Permite o cadastro contínuo de idades;
- Valida se a idade está dentro da faixa permitida;
- Ignora valores inválidos;
- Calcula a média das idades válidas registradas;
- Exibe o resultado ao final da execução.

Regras aplicadas:

- Idades entre **10 e 100 anos**:
  - São consideradas válidas e utilizadas no cálculo da média.

- Idades menores que **10** ou maiores que **100**:
  - São consideradas inválidas e ignoradas.

- Valor **0**:
  - Encerra o cadastro das idades.

## ✨ Funcionalidades

- Cadastro contínuo de idades;
- Validação automática dos dados;
- Cálculo da média das idades válidas;
- Contagem de registros válidos;
- Tratamento de entradas inválidas;
- Encerramento controlado do sistema.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Conversão de tipos (`int`);
- Estruturas de repetição:
  - `while`
- Estruturas condicionais:
  - `if`
  - `else`
- Operadores relacionais e lógicos;
- Controle de fluxo:
  - `break`
  - `continue`
- Variáveis acumuladoras;
- Contadores;
- Cálculo de média;
- Validação de dados;
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
📁 analise-idades-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o fortalecimento da lógica de programação, permitindo compreender a importância da validação de dados antes do processamento das informações.

Além disso, foi possível praticar o uso de acumuladores, contadores e estruturas de repetição para gerar indicadores estatísticos de forma simples e eficiente.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos fundamentais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**.

Embora seja um sistema simples, ele demonstra uma estrutura semelhante à utilizada em aplicações reais, nas quais dados precisam ser validados antes de serem armazenados e processados.

Como evolução futura, o projeto poderá ser expandido com:

- Cadastro do nome dos usuários;
- Armazenamento das idades em uma lista;
- Cálculo da maior e da menor idade;
- Geração de relatórios estatísticos;
- Exportação dos dados para arquivos;
- Organização do código utilizando funções e orientação a objetos.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**