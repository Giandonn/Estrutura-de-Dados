def inverter_string (string):
    pilha = []
    for letra in string:
        pilha.append(letra)
    while (len(pilha) > 0):
        elemento = pilha.pop(0)
        print(elemento, end="")

palavra = "estrutura"
print(palavra)
inverter_string(palavra)