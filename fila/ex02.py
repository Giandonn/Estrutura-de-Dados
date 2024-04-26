from time import sleep
pedidos = []
menu = """"
1 - incluir pedido
2- listar pedidos
3- processar pedidos
4- sair
"""

opcao = int(input("Digite sua opcao:"))

while opcao != "4":
    match(opcao):
        case "1":
            pedido = int(input("digite os produtos do pedido:"))
            if pedido != "":
                pedidos.append(pedido)
        case "2":
            for indice in range(0, len(pedidos)):
                print(f"pedido {indice + 1}: {pedidos[indice]}")
        case "3":
            print("PROCESSANDO LISTA DE PEDIDOS...")
            sleep(2)
            contador = 0
            while len(pedidos) > 0:
                print(f"preparando pediido: {contador + 1}...")
                sleep(2)
                print(f"pedido {contador + 1} processado com {pedido}")
                sleep(2)
                contador += 1
            print("lista de pedidos processada com sucesso")
    print(menu)
    opcao = input("digite sua opcao:")