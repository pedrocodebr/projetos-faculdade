turma_a = ["Ana", "Bruno", "Carlos"]
turma_b = ["Carlos", "Diana", "Eduarda"]

set_a = set(turma_a)
set_b = set(turma_b)

nas_duas = set_a & set_b
apenas_a = set_a - set_b
apenas_b = set_b - set_a

print("Nas duas turmas:", nas_duas)
print("Apenas na turma A:", apenas_a)
print("Apenas na turma B:", apenas_b)