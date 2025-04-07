import json

def carregar_reservas():
    try:
        with open('reservas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_reservas(reservas):
    with open('reservas.json', 'w') as f:
        json.dump(reservas, f)

def exibir_mapa_assentos():
    for assento, ocupado in mapa_assentos.items():
        status = 'Ocupado' if ocupado else 'Disponível'
        print(f"Assento {assento}: {status}")

def reservar_assento():
    assento = input("Digite o número do assento para reserva: ")
    if mapa_assentos.get(assento, False):
        print("Este assento já está reservado.")
    else:
        mapa_assentos[assento] = True
        salvar_reservas(mapa_assentos)
        print(f"Assento {assento} reservado com sucesso.")

def cancelar_reserva():
    assento = input("Digite o número do assento para cancelar a reserva: ")
    if mapa_assentos.get(assento, False):
        mapa_assentos[assento] = False
        salvar_reservas(mapa_assentos)
        print(f"Reserva do assento {assento} cancelada.")
    else:
        print("Este assento não está reservado.")

mapa_assentos = carregar_reservas()

while True:
    print("\n1. Exibir Mapa de Assentos")
    print("2. Reservar Assento")
    print("3. Cancelar Reserva")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        exibir_mapa_assentos()
    elif opcao == '2':
        reservar_assento()
    elif opcao == '3':
        cancelar_reserva()
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")
