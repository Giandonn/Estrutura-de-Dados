#undo redo

menu = """
1- realizar acao
2- desfazer acao
3- refazer acao
4- imprimir pilhas
5- sair
"""

desfazer = []
refazer = []
print(menu)
opcao = input("escolha uma opcao")

while opcao != 5:
    match opcao:
        case "1":
            acao = input("informe a acao")
            desfazer.append(acao)
            print("lista desfazer")
            imprimir_lista(desfazer)
            print("Lista refazer")
            imprimir_lista(refazer)
        case "2":
            acao = desfazer.pop()
            refazer.append(acao)
            print(f"acao {acao} desfeita")
        case "3":
            acao = refazer.pop()
            desfazer.append(acao)
            print(f"acao {acao} refeita")
