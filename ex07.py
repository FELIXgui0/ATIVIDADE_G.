print("\nExercício 7: Diferença entre quadrados dos ímpares")
numero = int(input("Digite um número ímpar: "))
if numero % 2 == 0:
    print("Número não é ímpar.")
else:
    anterior = (numero - 2)**2
    proximo = (numero + 2)**2
    diferenca = abs(anterior - proximo)
    print("Diferença entre os quadrados:", diferenca)