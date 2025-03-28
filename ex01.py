# 1. Cálculo de médias
notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(3)]
media_simples = sum(notas) / 3
media_ponderada_1 = (notas[0]*2 + notas[1]*2 + notas[2]*3) / 7
media_ponderada_2 = (notas[0]*1 + notas[1]*2 + notas[2]*2) / 5
print(f"Média simples: {media_simples}")
print(f"Média ponderada 1: {media_ponderada_1}")
print(f"Média ponderada 2: {media_ponderada_2}")

# 2. Conversão de segundos para dias, horas e minutos
segundos = int(input("Digite um valor em segundos: "))
dias = segundos // 86400
segundos %= 86400
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
print(f"{dias} dias, {horas} horas, {minutos} minutos")

# 3. Imposto sobre mercadorias
valor_total = float(input("Digite o valor total das mercadorias: R$"))
if valor_total > 500:
    imposto = (valor_total - 500) * 0.50
else:
    imposto = 0
print(f"Imposto: R${imposto}")

# 4. Custo total de aluguel de carro
dias = int(input("Digite o número de dias alugados: "))
km = float(input("Digite a quilometragem rodada: "))
custo = dias * 90
if km > 100:
    custo += (km - 100) * 12
print(f"Custo total: R${custo}")

# 5. Exibir os 100 primeiros números naturais
numeros_naturais = list(range(1, 101))
print(numeros_naturais)

# 6. Gerar e exibir os 100 primeiros números primos
primos = []
num = 2
while len(primos) < 100:
    divisor = 2
    eh_primo = True
    while divisor <= int(num ** 0.5):
        if num % divisor == 0:
            eh_primo = False
            break
        divisor += 1
    if eh_primo:
        primos.append(num)
    num += 1
print(primos)

# 7. Diferença entre quadrados dos ímpares
num = int(input("Digite um número ímpar: "))
if num % 2 == 0:
    print("Número não é ímpar.")
else:
    anterior = (num - 2)**2
    proximo = (num + 2)**2
    diferenca = abs(anterior - proximo)
    print(f"Diferença entre quadrados: {diferenca}")

# 8. Converter Celsius para Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"Temperatura em Fahrenheit: {fahrenheit}")

# 9. Maior e menor número
numeros = [float(input(f"Digite o número {i+1}: ")) for i in range(3)]
maior = numeros[0]
menor = numeros[0]
for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

# 10. Verificar número primo
num = int(input("Digite um número inteiro maior que 1: "))
divisor = 2
eh_primo = True
while divisor <= int(num**0.5):
    if num % divisor == 0:
        eh_primo = False
        break
    divisor += 1
if eh_primo:
    print("É primo.")
else:
    print("Não é primo.")

# 11. Sistema de login
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
if usuario == senha:
    print("Erro: Nome de usuário e senha não podem ser iguais.")
else:
    print("Login permitido.")

# 12. Média de alunos por turma
turmas = int(input("Digite a quantidade de turmas: "))
alunos_total = 0
for i in range(turmas):
    alunos = int(input(f"Digite o número de alunos da turma {i+1}: "))
    if alunos > 40:
        print(f"Turma {i+1} tem mais de 40 alunos.")
    alunos_total += alunos
media_alunos = alunos_total / turmas
print(f"Média de alunos por turma: {media_alunos}")

# 13. Salário após vários anos
salario = float(input("Digite o salário inicial: R$"))
anos = int(input("Digite o número de anos: "))
for ano in range(anos):
    salario *= 2
print(f"Salário após {anos} anos: R${salario}")
