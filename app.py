print("=== Projeto DevOps ===")
print("Aplicação iniciada com sucesso!")

tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    print("\n=== Lista de Tarefas ===")
    for tarefa in tarefas:
        print("-", tarefa)

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print("Tarefa removida com sucesso!")
    else:
        print("Tarefa não encontrada.")
