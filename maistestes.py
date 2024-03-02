import funcao_pesquisa_ordenacao
from time import perf_counter

lista = funcao_pesquisa_ordenacao.gera_lista_aleatoria(10, 1, 100)
print("lista gerada")
print(lista)

print("ordenando a lista")
lista.sort()
print("lista ordenada")
print(lista)