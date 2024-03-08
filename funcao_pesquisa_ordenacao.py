import random

def busca_binaria (valor, lista_ordenada):
    esquerda = 0
    direita = len(lista_ordenada) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if (valor == lista_ordenada[meio]):
            return meio
        elif valor < lista_ordenada[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return - 1


def gera_lista_aleatoria (tamanho, inicial, final):
    if (tamanho > final - inicial + 1):
        print("Tamanho deve ser menor igual ao intervalo")
        return
    lista = []
    atual = 0
    while atual < tamanho:
        valor = random.randint(inicial, final)
        if valor not in lista:
            lista.append(valor)
            atual += 1
    return lista

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

    