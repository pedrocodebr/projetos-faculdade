# 📌 Sistema de Login com Controle de Tentativas

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula um processo de autenticação simples, permitindo que o usuário informe uma senha e controlando a quantidade máxima de tentativas permitidas.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos de estruturas de repetição, estruturas condicionais e controle de fluxo, desenvolvendo uma solução capaz de validar credenciais e bloquear novas tentativas após um limite definido.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Define uma senha cadastrada no sistema;
- Solicita a senha informada pelo usuário;
- Compara a senha digitada com a senha correta;
- Permite até 3 tentativas de acesso;
- Libera o acesso caso a senha esteja correta;
- Bloqueia o acesso caso todas as tentativas sejam utilizadas.

Funcionamento:

- Senha correta:
  - O sistema informa que o login foi realizado com sucesso.

- Senha incorreta:
  - A tentativa é contabilizada e o usuário pode tentar novamente.

- Três tentativas inválidas:
  - O sistema informa que a conta foi bloqueada.

## ✨ Funcionalidades

- Validação de senha;
- Controle de quantidade de tentativas;
- Sistema de bloqueio após falhas;
- Mensagens de retorno ao usuário;
- Controle de acesso através de autenticação.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis;
- Entrada e saída de dados;
- Strings;
- Estruturas de repetição:
  - `while`
- Estruturas condicionais:
  - `if`
  - `else`
- Controle de fluxo:
  - `break`
- Contadores;
- Comparação de valores;
- Validação de informações;
- Simulação de autenticação.

## ▶️ Como Executar

1. Clone este repositório;
2. Abra a pasta do projeto;
3. Execute o arquivo principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
📁 sistema-login-python
├── main.py
└── README.md
```

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para a compreensão de como sistemas podem controlar acesso através da validação de informações fornecidas pelo usuário.

A implementação permitiu praticar conceitos importantes como contadores, limites de tentativas e controle de execução, utilizados frequentemente em sistemas de autenticação.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos iniciais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**.

Apesar de ser um sistema simples, apresenta uma lógica semelhante à utilizada em processos reais de login, onde informações precisam ser verificadas e acessos podem ser restringidos após múltiplas tentativas inválidas.

Como evolução futura, o projeto poderá ser expandido com:
- Cadastro de usuários;
- Criptografia de senhas;
- Banco de dados;
- Diferentes níveis de permissão;
- Sistema de recuperação de senha;
- Interface gráfica.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**
