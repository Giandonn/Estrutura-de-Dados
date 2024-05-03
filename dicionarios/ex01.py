def inverter_string (string):
    pilha = []
    for letra in string:
        pilha.append(letra)
    while (len(pilha) > 0):
        elemento = pilha.pop()
        print(elemento, end="")

palavra = "estrutura"
print(palavra)
inverter_string(palavra)