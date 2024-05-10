#versao 10 do python necessaria para usar o match
tarefas = {}
id_tarefa = 1

menu = """
1- adicionar tarefa
2- listar tarefas
5 - sair
"""

print(menu)

opcao = input("digite sua opcao")

while opcao != "5":
    match opcao:
        case "1":
            descricao = input("qual a descricao da tarefa")
            prioridade = input("digite a prioridade da tarefa: Falta, Media, Alta")
            tarefas[id_tarefa] = {"descricao": descricao, "prioridade": prioridade}
            id_tarefa += 1
        case "2":
            for id in tarefas:
                print(f"tarefa {id_tarefa}, {tarefas[id]["descricao"]}, prioridade {tarefas[id]["prioridade"]}")
    print(menu)
    opcao = input("Digite sua opcao: ")