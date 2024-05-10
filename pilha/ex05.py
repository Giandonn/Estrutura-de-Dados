<<<<<<< HEAD
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
=======
pilhaAcao = []
pilhaAcaoDesfeita = []

acao = input("Insira um texto: ")

if acao != "":
    pilhaAcao.append(acao)
    teste = len(pilhaAcao[0]) - 1
    print(f"ultimo elemento {teste}")
    print(f"pilha acao{pilhaAcao}")
    print(f"pilha acao desfeita{pilhaAcaoDesfeita}")

for i in pilhaAcao:
    i = len(pilhaAcao[0]) - 1
    print(i)  

lista = []

lista.append(10)
lista.append(20)

for i in len(lista):
	if lista[i] == 10:
		lista.pop()

print(lista)
>>>>>>> 3c44eb71ea3c2749a241e5d844e29b51bbc77793
