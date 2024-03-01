import random

def geraLista (tamanho, embaralhar = True):
    lista = []
    for i in range (1, tamanho + 1):
        lista.append(i)
    if embaralhar:
        random.shuffle(lista)
    return lista

def busca_sequencial (valor, lista):
    indice_atual = 0
    while indice_atual < len(lista):
        if lista[indice_atual] == valor:
            #encontrou
            return indice_atual

            #nao encontrei
        indice_atual += 1

    #terminou o laço... nao tem o elemento na lista
    #retorno -1 indicando que o valor nao existe na lista
    return - 1



