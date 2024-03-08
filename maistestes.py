import funcao_pesquisa_ordenacao
from time import perf_counter

lista = funcao_pesquisa_ordenacao.gera_lista_aleatoria(100000, 1, 100000)
print("lista gerada")
print(lista)

print("ordenando a lista")
lista.sort()
print("lista ordenada")
print(lista)

print("busca sequencial")
valor = 43789
inicio = perf_counter()
posicao = funcao_pesquisa_ordenacao.busca_sequencial(valor, lista)
fim = perf_counter()
tempo = fim - inicio
print(f"tempo {tempo:0.6f} segundos - pos:{posicao} {lista[posicao]}")

print("busca binária")
inicio = perf_counter()
posicao = funcao_pesquisa_ordenacao.busca_binaria(valor, lista)
fim = perf_counter()
tempo = fim - inicio
print(f"tempo {tempo:0.6f} segundos - pos:{posicao} {lista[posicao]}")