# Lista para armazenar os gastos (cada gasto será um dicionário com "descricao" e "valor")
gastos = []

# Função que exibe o menu principal do programa
def exibir_menu():
    print("\n-------- Controle de Gastos --------")
    print("1 - Adicionar gasto") # Permite adicionar um novo gasto
    print("2 - Visualizar gastos") # Mostra todos os gastos registrados
    print("3 - Remover gasto") # Remove um gasto da lista
    print("4 - Exibir total gasto")# Mostra o total gasto até o momento
    print("5 - Sair") # Encerra o programa
    print("------------------------------------")

# Função para adicionar um novo gasto à lista
def adicionar_gasto():
    descricao = input("Descrição do gasto: ") # Usuário informa do que se trata o gasto

    while True: # Laço para garantir que o valor inserido seja válido
        try:
            valor = float(input("Valor do gasto (R$): ")) # Usuário insere o valor
            break # Se a conversão para float funcionar, sai do loop
        except ValueError:
            print("Por favor, insira um valor válido!") # Caso o usuário digite algo inválido

    # Adiciona um dicionário com os detalhes do gasto à lista
    gastos.append({"descricao": descricao, "valor": valor})
    print("✅ Gasto adicionado com sucesso!")

# Função para exibir todos os gastos cadastrados
def visualizar_gastos():
    if not gastos: # Se a lista de gastos estiver vazia, exibe a mensagem
        print("Nenhum gasto registrado ainda.")
        return

    print("\n📜 Lista de Gastos:")
    for i, gasto in enumerate(gastos): # Percorre a lista mostrando cada gasto
        print(f"{i+1}. {gasto['descricao']} - R$ {gasto['valor']:.2f}")

# Função para remover um gasto específico
def remover_gasto():
    visualizar_gastos() # Exibe a lista para que o usuário saiba qual remover
    if not gastos: # Se não houver gastos, retorna sem fazer nada
        return

    try:
        indice = int(input("Digite o número do gasto para remover: ")) - 1
        if 0 <= indice < len(gastos): # Verifica se o número digitado é válido
            removido = gastos.pop(indice) # Remove o gasto da lista
            print(f"❌ Gasto '{removido['descricao']}' removido!")
        else:
            print("Número inválido!") # Caso o número digitado não corresponda a um gasto válido
    except ValueError:
        print("Digite um número válido!") # Caso o usuário digite algo que não seja um número

# Função para calcular e exibir o total gasto até o momento
def exibir_total():
    total = sum(gasto["valor"] for gasto in gastos) # Soma os valores dos gastos registrados
    print(f"\n💰 Total gasto: R$ {total:.2f}")

# Loop principal do programa, que mantém o menu ativo até o usuário escolher sair
while True:
    try:
        exibir_menu() # Mostra o menu para o usuário
        opcao = int(input(": ")) # Usuário escolhe uma opção

        if opcao not in range(1, 6): # Garante que a opção esteja entre 1 e 5
            print("Insira um número de 1 até 5!\n")
            continue # Volta ao início do loop sem executar o match-case

        # Estrutura match-case para executar a ação correspondente à opção escolhida
        match opcao:
            case 1:
                adicionar_gasto() # Chama a função para adicionar um gasto
            case 2:
                visualizar_gastos() # Chama a função para visualizar os gastos
            case 3:
                remover_gasto() # Chama a função para remover um gasto
            case 4:
                exibir_total() # Chama a função para exibir o total gasto
            case 5:
                print("Saindo do programa...") # Mensagem de saída
                break # Encerra o loop, finalizando o programa

    except ValueError:
        print("Digite um NÚMERO de 1 até 5, por favor não insira letras!\n") # Tratamento de erro caso o usuário digite algo inválido