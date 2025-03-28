print("\nExercício 10: Verificar se é primo")
numero = int(input("Digite um número inteiro maior que 1: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break
if primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
