print("\nExercício 12: Média de alunos por turma")
turmas = int(input("Digite o número de turmas: "))
alunos_totais = 0
for i in range(turmas):
    alunos = int(input(f"Digite o número de alunos da turma {i+1}: "))
    alunos_totais += alunos
media_alunos = alunos_totais / turmas
print("Média de alunos por turma:", media_alunos)