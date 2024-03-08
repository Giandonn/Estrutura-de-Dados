from time import perf_counter

inicio = perf_counter()

#inicio do algoritmo
acumulador = 0
for i in range(10000000):
    acumulador += 1

#fim do algoritmo
fim = perf_counter()

tempo = fim - inicio
print(f"algoritmo exec em: {tempo: 0.6f} segundos")