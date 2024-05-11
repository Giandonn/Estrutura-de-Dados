lista = {
    "produto": {},
    "quantidade": {}
}

produto = input("digite qual produto deseja adicionar: ")
quantidade = int(input("digite a quantidade que deseja adicionar: "))

lista["produto"] = produto
lista["quantidade"] = quantidade

print(lista)