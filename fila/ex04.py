from time import sleep
import random

spool = []
menu = """
FILA DE IMPRESSAO

1- IMPRIMIR DOCUMENTO
2- MOSTRAR FILA DE PRESSAO
3- PROCESSAR FILA
4- SAIR
"""
print(menu)

opcao = input("informe a opcao:")

while opcao != "4":
    match opcao:
        case "1":
            arquivo = input("arquivo para a impressao")
            if arquivo != "":
                spool.append(arquivo)
        case "2":
            num_doc = 1
            for documento in spool:
                print(f"{num_doc}: {documento}")
                documento += 1
        case "3":
            print("INICIANDO IMPRESSAO DE FILA DE DOCUMENTOS")
            while len(spool) > 0:
                documento_atual = spool.pop(0)
                print(f"imprimindo {documento_atual}")
                paginas = random.randint(1, 10)
                for pagina in range (1, paginas + 1):
                    print(f"  imprimindo pagina {pagina}/{paginas}")
                    sleep(1)
                print(f"Documento {documento_atual} impresso!")