# 📌 Sistema de Análise de Notas

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema permite registrar notas de alunos, calcular automaticamente a média da turma e identificar quantos estudantes obtiveram desempenho acima da média.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como listas, estruturas de repetição, estruturas condicionais e validação de dados, por meio da implementação de um sistema capaz de armazenar informações e gerar indicadores de desempenho.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita as notas dos alunos;
- Valida se cada nota está entre 0 e 10;
- Armazena apenas notas válidas em uma lista;
- Permite encerrar o cadastro informando **-1**;
- Calcula a média das notas registradas;
- Conta quantos alunos obtiveram nota acima da média;
- Exibe um resumo com os resultados.

### Regras aplicadas

- **Notas entre 0 e 10:**
  - São consideradas válidas e armazenadas.

- **Notas menores que 0 ou maiores que 10:**
  - São consideradas inválidas e ignoradas.

- **Valor -1:**
  - Encerra o cadastro das notas.

## ✨ Funcionalidades

- Cadastro contínuo de notas;
- Validação automática dos valores informados;
- Armazenamento das notas em lista;
- Cálculo automático da média da turma;
- Contagem de alunos acima da média;
- Exibição de um resumo estatístico.

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
📁 analise-notas-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o fortalecimento da lógica de programação, permitindo aplicar conceitos de validação de dados, armazenamento em listas e processamento de informações para geração de indicadores estatísticos.

Além disso, possibilitou praticar estruturas de repetição, cálculo de médias e comparação de valores, técnicas frequentemente utilizadas em sistemas acadêmicos e de gestão.

## 💭 Considerações Finais

Este projeto representa uma evolução nos estudos de programação em Python durante minha formação em **Análise e Desenvolvimento de Sistemas**. Apesar de sua simplicidade, demonstra a utilização de estruturas de dados para armazenamento de informações e o processamento dessas informações para obtenção de resultados relevantes.

Como melhoria futura, o sistema poderá ser expandido para permitir o cadastro do nome dos alunos, cálculo da maior e da menor nota, classificação por desempenho, geração de boletins e armazenamento das informações em arquivos ou banco de dados.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**