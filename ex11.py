print("\nExercício 11: Sistema de login")
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
if usuario == senha:
    print("Erro: Nome de usuário e senha não podem ser iguais.")
else:
    print("Login permitido.")
