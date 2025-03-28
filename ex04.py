print("\nExercício 4: Custo total de aluguel de carro")
dias = int(input("Digite o número de dias alugados: "))
km = float(input("Digite a quilometragem rodada: "))
custo = dias * 90
if km > 100:
    custo += (km - 100) * 12
print("Custo total do aluguel: R$", custo)