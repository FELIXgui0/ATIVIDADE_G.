dias = int(input("Digite o número de dias: "))
km_rodados = float(input("Digite o número de quilômetros rodados: "))

custo_diario = 90 * dias
if km_rodados > 100:
    custo_extra = (km_rodados - 100) * 12
else:
    custo_extra = 0

total = custo_diario + custo_extra
print(f"Valor total a ser pago: R${total:.2f}")
