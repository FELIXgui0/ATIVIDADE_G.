def conta_caracteres(frase):
    return len(frase.replace(" ", ""))

frase = "Olá mundo!"
print("Número de caracteres (sem espaços):", conta_caracteres(frase))
