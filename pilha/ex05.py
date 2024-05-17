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
