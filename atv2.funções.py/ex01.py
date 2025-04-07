import json
from datetime import datetime

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as f:
        json.dump(tarefas, f)

def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    prazo = input("Prazo (AAAA-MM-DD): ")
    tarefa = {"descricao": descricao, "prazo": prazo, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

def listar_tarefas():
    tarefas_ordenadas = sorted(tarefas, key=lambda t: t['prazo'])
    for t in tarefas_ordenadas:
        status = "Concluída" if t["concluida"] else "Pendente"
        print(f"{t['descricao']} - Prazo: {t['prazo']} - Status: {status}")

def concluir_tarefa():
    descricao = input("Descrição da tarefa a ser concluída: ")
    for t in tarefas:
        if t["descricao"] == descricao and not t["concluida"]:
            t["concluida"] = True
            salvar_tarefas(tarefas)
            print(f"Tarefa '{descricao}' concluída.")
            return
    print("Tarefa não encontrada ou já concluída.")

tarefas = carregar_tarefas()

while True:
    print("\n1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_tarefa()
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        concluir_tarefa()
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")
