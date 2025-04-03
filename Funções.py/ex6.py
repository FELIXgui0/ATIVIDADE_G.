def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

frase = "Exemplo de texto"
print("Número de vogais:", conta_vogais(frase))
