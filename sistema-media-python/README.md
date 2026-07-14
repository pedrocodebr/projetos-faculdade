# 📌 Sistema Media Python

## 📖 Descrição
Este projeto foi desenvolvido durante minhas atividades de estudos na disciplina Análise e Desenvolvimento de Sistemas (ADS) para ilustrar a criação de um simples sistema de gerenciamento de mídia. O objetivo é demonstrar o uso de estruturas de dados, funções, laços e bibliotecas em Python.

## 🎯 Objetivo
O projeto teve como objetivo praticar conceitos importantes da programação, incluindo a manipulação de listas, dicionários, funções, loops e a utilização de módulos padrão do Python.

## 📝 Sobre o Projeto
- **Entrada**: O sistema aceita uma lista de mídias (várias strings) como entrada.
- **Processamento**: O programa organiza essas mídias em categorias de acordo com seu tipo (vídeo, música, livro).
- **Saída**: A saída é um dicionário onde as chaves são os tipos de mídia e os valores são listas dos nomes das mídias pertencentes a cada categoria.

### Exemplo de Entrada
```python
midias = ["Videio1.mp4", "Musica2.mp3", "Livro3.pdf"]
```

### Exemplo de Saída
```python
{
    'vídeo': ['Videio1'],
    'música': ['Musica2'],
    'livro': ['Livro3']
}
```

## ✨ Funcionalidades
- **Criação de categorias**: A função `organizar_midias` organiza as mídias em categorias com base no tipo.
- **Exibição dos resultados**: O resultado é exibido em forma de um dicionário.

## 🛠️ Tecnologias Utilizadas
- Python 3.x

## 🧠 Conceitos Praticados
- Estruturas de Dados (Listas, Dicionários)
- Funções
- Laços (for, if)
- Bibliotecas Padrão do Python

## ▶️ Como Executar
1. Clonar o repositório ou copiar o código.
2. Certificar-se de ter o Python 3.x instalado.
3. Executar o script `organizador.py`.

```bash
python organizador.py
```

## 📂 Estrutura do Projeto
```
organizador/
├── organizador.py
└── README.md
```

## 📚 Aprendizados
- Praticar a manipulação de estruturas de dados em Python.
- Entender como usar funções para modularizar o código.
- Aprender sobre a importância da organização de arquivos em projetos.

## 💭 Considerações Finais
Este projeto foi uma excelente oportunidade para aplicar conceitos teóricos aprendidos em sala de aula. Foi gratificante ver como essas teorias se concretizam em código funcional. Posso imaginar que este sistema pode ser estendido para incluir mais funcionalidades, como filtros adicionais e interações com o usuário.

## 👨‍💻 Autor
**Pedro Santos**

---

Código do projeto (analise para extrair nomes de arquivos, bibliotecas e lógica real, não invente funcionalidades que não existem no código):
```python
def organizar_midias(midias):
    categorias = {
        'vídeo': [],
        'música': [],
        'livro': []
    }
    
    for midia in midias:
        if midia.endswith('.mp4') or midia.endswith('.avi'):
            categorias['vídeo'].append(midia)
        elif midia.endswith('.mp3') or midia.endswith('.wav'):
            categorias['música'].append(midia)
        elif midia.endswith('.pdf') or midia.endswith('.epub'):
            categorias['livro'].append(midia)
    
    return categorias

midias = ["Videio1.mp4", "Musica2.mp3", "Livro3.pdf"]
print(organizar_midias(midias))
```

Resposta APENAS com o conteúdo do README.md em markdown puro, sem comentários fora do markdown, sem envolver tudo em blocos ```markdown.