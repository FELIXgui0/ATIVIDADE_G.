valor_total = float(input("Digite o valor total das mercadorias: "))

if valor_total < 500:
    imposto = 0
else:
    imposto = (valor_total - 500) * 0.5

print(f"Imposto a ser pago: R${imposto:.2f}")
