# 📌 Sistema de Autenticação de Login

## 📖 Descrição

Este projeto foi desenvolvido durante os estudos da disciplina de Programação em Python do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O sistema simula um processo de autenticação de usuários, permitindo um número limitado de tentativas para inserção da senha antes de bloquear o acesso.

## 🎯 Objetivo

O objetivo deste projeto foi aplicar conceitos fundamentais da linguagem Python, como estruturas de repetição, estruturas condicionais e controle de fluxo, por meio da implementação de um sistema simples de autenticação de usuários.

## 📝 Sobre o Projeto

O programa realiza as seguintes etapas:

- Solicita a senha ao usuário;
- Compara a senha informada com a senha cadastrada;
- Permite até três tentativas de autenticação;
- Informa quando a senha está incorreta;
- Libera o acesso caso a senha esteja correta;
- Bloqueia a conta quando o limite de tentativas é atingido.

### Regras aplicadas

- **Senha correta:**
  - O acesso é liberado imediatamente.

- **Senha incorreta:**
  - O número de tentativas é incrementado.

- **Três tentativas incorretas:**
  - A conta é bloqueada automaticamente.

## ✨ Funcionalidades

- Simulação de autenticação de usuários;
- Controle do número de tentativas;
- Bloqueio automático após três erros;
- Validação de senha;
- Mensagens informativas ao usuário.

## 🛠️ Tecnologias Utilizadas

- Python 3

## 🧠 Conceitos Praticados

- Variáveis
- Entrada e saída de dados
- Estruturas de repetição (`while`)
- Estruturas condicionais (`if` e `else`)
- Controle de fluxo (`break`)
- Operadores relacionais
- Operadores lógicos
- Contadores
- Comparação de strings

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

O desenvolvimento deste projeto contribuiu para o fortalecimento da lógica de programação, permitindo compreender como sistemas de autenticação controlam tentativas de acesso e aplicam regras de segurança para proteger informações.

Além disso, possibilitou praticar o uso de estruturas de repetição, contadores e condições para controlar o fluxo de execução de um programa.

## 💭 Considerações Finais

Este projeto representa uma aplicação prática dos conceitos fundamentais de programação em Python desenvolvidos durante minha formação em **Análise e Desenvolvimento de Sistemas**. Apesar de sua simplicidade, demonstra a lógica utilizada em sistemas de autenticação presentes em aplicações web, sistemas corporativos e plataformas digitais.

Como melhoria futura, o sistema poderá ser expandido para permitir:

- Cadastro de múltiplos usuários;
- Ocultação da senha durante a digitação;
- Definição de senhas criptografadas;
- Recuperação de senha;
- Registro de tentativas de acesso;
- Armazenamento de usuários em banco de dados;
- Organização do código utilizando funções e orientação a objetos.

## 👨‍💻 Autor

**Pedro Leonardo Piancó Tenório**
