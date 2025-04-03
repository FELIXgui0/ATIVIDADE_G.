def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return f"Média: {media:.2f}. Aprovado!"
    else:
        return f"Média: {media:.2f}. Reprovado!"

print(calcula_media(8, 7, 6))
