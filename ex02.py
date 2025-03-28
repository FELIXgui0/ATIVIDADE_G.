print("\nExercício 2: Conversão de segundos para dias, horas e minutos")
segundos = int(input("Digite o valor em segundos: "))
dias = segundos // 86400
segundos = segundos % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
print(f"{dias} dias, {horas} horas, {minutos} minutos")