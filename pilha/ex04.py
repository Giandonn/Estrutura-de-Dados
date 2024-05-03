def verificaParenteses (parenteses) :
    pilha = []
    if parenteses != "":
        pilha.append(parenteses)
        print(pilha)
    else :
        print("nao é possivel verificar vazio")

    if pilha[0][0] == "(" and pilha[0][6] == ")":
        print("parenteses equilibrado")
    else:
        print("parenteses nao equiblibrado")

verificaParenteses("(teste)")