salario = float(input("Digite o salário inicial: R$"))
anos = int(input("Digite o número de anos: "))
for ano in range(anos):
    salario *= 2
print(f"Salário após {anos} anos: R${salario}")