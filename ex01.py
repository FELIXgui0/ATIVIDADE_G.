nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_aritmetica = (nota1 + nota2 + nota3) / 3
media_ponderada1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / (2 + 2 + 3)
print(f"Média Ponderada (pesos 2, 2, 3): {media_ponderada1:.2f}")
media_ponderada2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / (1 + 2 + 2)
print(f"Média Ponderada (pesos 1, 2, 2): {media_ponderada2:.2f}")

