import json

def carregar_estoque():
    try:
        with open('estoque.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open('estoque.json', 'w') as f:
        json.dump(estoque, f)

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(produto)
    salvar_estoque(estoque)

def exibir_estoque():
    total = 0
    for p in estoque:
        print(f"{p['nome']} - Quantidade: {p['quantidade']} - Preço: {p['preco']}")
        total += p['quantidade'] * p['preco']
    print(f"Valor total do estoque: {total}")

estoque = carregar_estoque()

while True:
    print("\n1. Adicionar Produto")
    print("2. Exibir Estoque")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        exibir_estoque()
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")
