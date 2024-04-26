import random

def gera_lista_aleatoria_com_repeticao(tamanho, valor_inicial, valor_final):
    """ 
        Gera uma lista de "tamanho" elementos aleatórios com valores 
        entre valor_inicial e valor_final
    """
    lista = []
    atual = 0
    while atual < tamanho:
        valor = random.randint(valor_inicial, valor_final)
        lista.append(valor)
        atual += 1
    return lista

def gera_lista_aleatoria(tamanho, valor_inicial, valor_final):
    """ 
        Gera uma lista de "tamanho" elementos aleatórios com valores 
        entre valor_inicial e valor_final
    """
    if tamanho > valor_final - valor_inicial + 1:
        print(f"Para gerar a lista é necessário {tamanho} valores possíveis")
        return
    lista = []
    atual = 0
    while atual < tamanho:
        valor = random.randint(valor_inicial, valor_final)
        if valor not in lista:
            lista.append(valor)
            atual += 1
    return lista

def busca_binaria(valor, lista_ordenada):
    esquerda = 0
    direita = len(lista_ordenada) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if valor == lista_ordenada[meio]:
            return meio
        elif valor < lista_ordenada[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1

def busca_sequencial(valor, lista):
    """ Busca por "valor" em "lista" de forma sequencial.
    Se encontrar, retorna seu índice na lista. Caso contrário, 
    retorna -1. """
    indice_atual = 0
    while indice_atual < len(lista):
        if lista[indice_atual] == valor:
            return indice_atual
        indice_atual += 1
    return -1