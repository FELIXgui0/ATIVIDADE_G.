import json

def carregar_contatos():
    try:
        with open('contatos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open('contatos.json', 'w') as f:
        json.dump(contatos, f)

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    salvar_contatos(contatos)

def buscar_contato():
    nome = input("Nome para buscar: ")
    for c in contatos:
        if nome.lower() in c['nome'].lower():
            print(f"Nome: {c['nome']}, Telefone: {c['telefone']}, Email: {c['email']}")
            return
    print("Contato não encontrado.")

contatos = carregar_contatos()

while True:
    print("\n1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        buscar_contato()
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")
