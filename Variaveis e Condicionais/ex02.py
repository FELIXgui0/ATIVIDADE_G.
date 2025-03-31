segundos = int(input("Digite o valor em segundos: "))
dias = segundos // 86400
segundos_restantes = segundos % 86400
horas = segundos_restantes // 3600
segundos_restantes %= 3600
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_final} segundos")
