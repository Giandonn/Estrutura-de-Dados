#verificando parenteses

def verificarParenteses (expressao):
    pilha = []
    indice = 0
    while indice < len(expressao):
        simbolo = expressao[indice]
        if simbolo == "(":
            pilha.append(simbolo)
        else:
            if len(pilha) == 0:
                print("expressao nao balanceada")
                break
            else:
                pilha.pop()
        indice += 1
    if len(pilha) == 0:
        print("expressao balanceada")
    else:
        print("expressao nao balanceada")

expressao1 = ")()"
print(expressao1)
verificarParenteses(expressao1)