while True:
    try:
        primeira_resposta_do_menu = int(input(f"--------Menu-------- \n1 - tralala \n2 - titiriri \n3 - tralarerotralala \n4 - aiaiaiaiaaiaai \n--------------------- \n:"))
        if primeira_resposta_do_menu > 0 and primeira_resposta_do_menu < 5:
            break
        else:
            print("insira um valor de 1 até 4!! \n. \n. \n.")
    except ValueError:
        print("Digite um NÚMERO de 1 até 4, por favor não insira letras!!\n. \n. \n.")
