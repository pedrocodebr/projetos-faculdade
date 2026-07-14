cursos = {
    "Python": {"vagas": 3, "preco": 120.0},
    "Java": {"vagas": 0, "preco": 150.0},
    "Banco de Dados": {"vagas": 5, "preco": 200.0}
}

mais_caro = ("", 0)

for curso, dados in cursos.items():
    if dados["vagas"] == 0:
        continue
    
    print(curso, "- R$", dados["preco"])
    
    if dados["preco"] > mais_caro[1]:
        mais_caro = (curso, dados["preco"])

print("Curso mais caro:", mais_caro)