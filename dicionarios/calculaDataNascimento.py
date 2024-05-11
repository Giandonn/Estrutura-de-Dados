from datetime import datetime

def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    hoje = datetime.now()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

pessoas = {}

while True:
    print("\nMenu:")
    print("1. Adicionar pessoa")
    print("2. Calcular idade")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome da pessoa: ")
        data_nascimento = input("Digite a data de nascimento (no formato AAAA-MM-DD): ")
        pessoas[nome] = data_nascimento
        print("Pessoa adicionada com sucesso!")

    elif opcao == '2':
        for nome, data_nascimento in pessoas.items():
            idade = calcular_idade(data_nascimento)
            print(f"{nome} tem {idade} anos.")

    elif opcao == '3':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
