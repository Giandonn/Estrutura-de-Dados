
def lista():
    tamanho = [0,1,2,3,4,5]
    valor = 5
    for i in tamanho:
        if valor == tamanho[i]:
            print(f"o valor {valor} existe na lista na posicao {tamanho[i]}")
lista()