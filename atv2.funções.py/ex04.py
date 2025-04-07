import json

def carregar_usuarios():
    try:
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        print("Login bem-sucedido.")
        return usuario
    else:
        print("Usuário ou senha inválidos.")
        return None

def realizar_transacao(usuario):
    tipo = input("Depósito ou Saque? (d/s): ")
    valor = float(input("Valor: "))
    if tipo == 'd':
        usuarios[usuario]['saldo'] += valor
    elif tipo == 's' and usuarios[usuario]['saldo'] >= valor:
        usuarios[usuario]['saldo'] -= valor
    else:
        print("Saldo insuficiente ou opção inválida.")
        return
    print(f"Novo saldo: {usuarios[usuario]['saldo']}")
    salvar_usuarios(usuarios)

usuarios = carregar_usuarios()

while True:
    print("\n1. Login")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        usuario_logado = login()
        if usuario_logado:
            while True:
                print("\n1. Realizar Transação")
                print("2. Sair")
                sub_opcao = input("Escolha uma opção: ")
                
                if sub_opcao == '1':
                    realizar_transacao(usuario_logado)
                elif sub_opcao == '2':
                    break
                else:
                    print("Opção inválida.")
    elif opcao == '2':
        break
    else:
        print("Opção inválida.")
