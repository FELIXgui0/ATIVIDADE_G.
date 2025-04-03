def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

print("É palíndromo?", eh_palindromo("arara"))
