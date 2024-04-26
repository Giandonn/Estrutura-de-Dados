fila = ['maria', 'joao', 'sebastiao', 'maricota']

while len(fila) > 0:
    atendido = fila.pop(0)
    print(f"a pessoa: {atendido} foi atendida")
    print(fila)