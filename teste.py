import funcao_pesquisa_ordenacao
from time import perf_counter

print("gerando a lista")
lista = funcao_pesquisa_ordenacao.geraLista(10000000)
print("lista gerada")

valor = 267789

print("iniciando a busca...")
inicio = perf_counter()
posicao = funcao_pesquisa_ordenacao.busca_sequencial(26789, lista)
fim = perf_counter()
print("busca finalizada")

tempo = fim - inicio
print(f"valor {valor} encontrado em {tempo:0.6f} segundos")
print(f"na posicao {posicao}: {lista[posicao]}")