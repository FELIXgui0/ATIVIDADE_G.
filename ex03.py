print("\nExercício 3: Imposto sobre mercadorias")
valor_total = float(input("Digite o valor total das mercadorias: R$"))
if valor_total > 500:
    imposto = (valor_total - 500) * 0.50
else:
    imposto = 0
print("Imposto: R$", imposto)
