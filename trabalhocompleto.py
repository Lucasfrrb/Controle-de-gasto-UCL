import json

ARQUIVO_GASTOS = "gastos.json"

gastos = []

def carregar_gastos():
    global gastos
    try:
        with open(ARQUIVO_GASTOS, "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        gastos = []

def salvar_gastos():
    with open(ARQUIVO_GASTOS, "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, indent=4)

def exibir_menu():
    print("\n-------- Controle de Gastos --------")
    print("1 - Adicionar gasto")
    print("2 - Visualizar gastos")
    print("3 - Remover gasto")
    print("4 - Exibir total gasto")
    print("5 - Sair")
    print("------------------------------------")

def adicionar_gasto():
    descricao = input("Descrição do gasto: ")
    while True:
        try:
            valor = float(input("Valor do gasto (R$): "))
            break
        except ValueError:
            print("Por favor, insira um valor válido!")
    gastos.append({"descricao": descricao, "valor": valor})
    salvar_gastos()
    print("✅ Gasto adicionado com sucesso!")

def visualizar_gastos():
    if not gastos:
        print("Nenhum gasto registrado ainda.")
        return
    print("\n📜 Lista de Gastos:")
    for i, gasto in enumerate(gastos):
        print(f"{i+1}. {gasto['descricao']} - R$ {gasto['valor']:.2f}")

def remover_gasto():
    visualizar_gastos()
    if not gastos:
        return
    try:
        indice = int(input("Digite o número do gasto para remover: ")) - 1
        if 0 <= indice < len(gastos):
            removido = gastos.pop(indice)
            salvar_gastos()
            print(f"❌ Gasto '{removido['descricao']}' removido!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido!")

def exibir_total():
    total = sum(gasto["valor"] for gasto in gastos)
    print(f"\n💰 Total gasto: R$ {total:.2f}")

carregar_gastos()

while True:
    try:
        exibir_menu()
        opcao = int(input(": "))
        if opcao not in range(1, 6):
            print("Insira um número de 1 até 5!\n")
            continue
        match opcao:
            case 1:
                adicionar_gasto()
            case 2:
                visualizar_gastos()
            case 3:
                remover_gasto()
            case 4:
                exibir_total()
            case 5:
                print("Saindo do programa...")
                break
    except ValueError:
        print("Digite um NÚMERO de 1 até 5, por favor não insira letras!\n")
