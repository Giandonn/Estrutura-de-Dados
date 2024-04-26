# import funcao_pesquisa_ordenacao
# from time import perf_counter

# print("gerando a lista")
# lista = funcao_pesquisa_ordenacao.geraLista(10000000)
# print("lista gerada")

# valor = 267789

# print("iniciando a busca...")
# inicio = perf_counter()
# posicao = funcao_pesquisa_ordenacao.      busca_sequencial(26789, lista)
# fim = perf_counter()
# print("busca finalizada")

# tempo = fim - inicio
# print(f"valor {valor} encontrado em {tempo:0.6f} segundos")
# print(f"na posicao {posicao}: {lista[posicao]}")

#exercicio 1
import funcoes
from time import perf_counter

array = funcoes.gera_lista_aleatoria(10, 0, 10)
posicao = 0
menorValor = array[0]

for index in range (len(array)):
    if (menorValor > array[index]):
        menorValor = array[index]
        posicao = index
    else:
        menorValor = menorValor
print(array)
print(f"O menor valor é: {menorValor}, a posição do menor valor é: {posicao}")

array2 = funcoes.gera_lista_aleatoria(10, 0, 10)
posicao2 = 0
menorValor2 = array[0]

for index in range (len(array)):
    if (menorValor2 < array[index]):
        menorValor2 = array[index]
        posicao2 = index
    else:
        menorValor2 = menorValor2
print(array)
print(f"O menor valor é: {menorValor}, a posição do menor valor é: {posicao}")

# lista = funcoes.gera_lista_aleatoria(10, 0, 100)

# # Inicializar as variáveis para os três maiores valores
# lista = funcoes.gera_lista_aleatoria(10, 0, 100)

# ouro = float('-inf')
# prata = float('-inf')
# bronze = float('-inf')

# for valor in lista:
#     if valor > ouro:
#         bronze = prata
#         prata = ouro
#         ouro = valor
#     elif valor > prata:
#         bronze = prata
#         prata = valor
#     elif valor > bronze:
#         bronze = valor

# print("Lista gerada aleatoriamente:", lista)
# print("Medalha de ouro:", ouro)
# print("Medalha de prata:", prata)
# print("Medalha de bronze:", bronze)


