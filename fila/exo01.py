fila = []
fila.append(5)
fila.append(10)
fila.append(15)
print(fila)

while len(fila) > 0:
    elemento = fila.pop(0)
    print(f"{elemento}: foi deletado da fila")

print(fila)