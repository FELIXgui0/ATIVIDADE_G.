n = int(input("Digite um número ímpar: "))

n_anterior = n - 2
n_proximo = n + 2
diferenca = (n_proximo ** 2) - (n_anterior ** 2)

print(f"Diferença entre os quadrados: {diferenca}")
