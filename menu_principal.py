def exibir_menu():    #definir a função exibir_menu
    print("\n-------- Menu --------")
    print("1 - tralala")
    print("2 - titiriri")
    print("3 - tralarerotralala")
    print("4 - aiaiaiaiaaiaai")
    print("5 - Sair")
    print("----------------------")

while True:  #repetir o menu até que o usuário escolha a opção 5
    try:
        exibir_menu()
        opcao = int(input(": "))

        if opcao not in range(1, 6):    #usar range para verificar se o número está dentro do intervalo   
            print("Insira um número de 1 até 5!\n")
            continue  # Volta para o início do loop sem executar o match-case

        match opcao: #usar match para verificar a opção escolhida
            case 1:
                print("tralala")
            case 2:
                print("titiriri")
            case 3:
                print("tralarerotralala")
            case 4:
                print("aiaiaiaiaaiaai")
            case 5:
                print("Saindo do programa...")
                break  # Sai do menu e encerra o programa

    except ValueError: #garantir que o usuário insira um número e nao use uma letra
        print("Digite um NÚMERO de 1 até 5, por favor não insira letras!\n")
