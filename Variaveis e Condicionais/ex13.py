salario = float(input("Digite o salário inicial: "))
anos = int(input("Digite o número de anos: "))

for _ in range(anos):
    salario *= 2

print(f"Salário após {anos} anos: R${salario:.2f}")
