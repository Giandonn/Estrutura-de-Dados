pilha = []
pilha.append(5)
pilha.append(10)
pilha.append(15)
print(pilha)

while len(pilha) > 0:
    elemento = pilha.pop()
    print(f"{elemento}: foi deletado da pilha")

print(pilha)