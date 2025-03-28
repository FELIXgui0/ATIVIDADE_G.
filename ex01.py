print("Exercício 1: Cálculo de Médias")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_simples = (nota1 + nota2 + nota3) / 3
media_ponderada_1 = (nota1*2 + nota2*2 + nota3*3) / 7
media_ponderada_2 = (nota1*1 + nota2*2 + nota3*2) / 5
print("Média simples:", media_simples)
print("Média ponderada 1:", media_ponderada_1)
print("Média ponderada 2:", media_ponderada_2)
