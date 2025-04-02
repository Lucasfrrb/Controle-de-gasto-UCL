import json
import calendar
import re
import matplotlib.pyplot as plt

ARQUIVO_GASTOS = "gastos.json"

gastos = {}
renda_mensal = 0

def carregar_gastos():
    global gastos, renda_mensal
    try:
        with open(ARQUIVO_GASTOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            gastos = dados.get("gastos", {})
            renda_mensal = dados.get("renda_mensal", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        gastos = {}
        renda_mensal = 0

def salvar_gastos():
    with open(ARQUIVO_GASTOS, "w", encoding="utf-8") as arquivo:
        json.dump({"gastos": gastos, "renda_mensal": renda_mensal}, arquivo, indent=4)

def definir_renda_mensal():
    global renda_mensal
    while True:
        valor = input("Digite sua renda mensal (R$) ou 0 para cancelar: ")
        if valor == "0":
            print("Alteração de renda cancelada.")
            return
        try:
            renda_mensal = float(valor)
            salvar_gastos()
            print("✅ Renda mensal atualizada!")
            break
        except ValueError:
            print("Por favor, insira um valor válido!")

def calcular_saldo_disponivel(mes):
    total_gastos = sum(gasto["valor"] for gasto in gastos.get(mes, []))
    total_retornos = sum(gasto["retorno"] for gasto in gastos.get(mes, []))
    return renda_mensal + total_retornos - total_gastos

def visualizar_gastos(mes):
    if mes not in gastos or not gastos[mes]:
        print("Nenhum gasto registrado ainda.")
        return
    print(f"\n📜 Lista de Gastos ({mes}):")
    for i, gasto in enumerate(gastos[mes]):
        tipo = "(Fixo)" if gasto["fixo"] else "(Variável)"
        retorno = f"| Retorno esperado: R$ {gasto['retorno']:.2f}" if gasto["retorno"] > 0 else ""
        print(f"{i+1}. {gasto['descricao']} - R$ {gasto['valor']:.2f} {tipo} {retorno}")

def adicionar_gasto(mes):
    descricao = input("Descrição do gasto: ")
    while True:
        try:
            valor = float(input("Valor do gasto (R$): "))
            break
        except ValueError:
            print("Por favor, insira um valor válido!")
    while True:
        tipo = input("O gasto é fixo? (s/n): ").strip().lower()
        if tipo in ('s', 'n'):
            fixo = tipo == 's'
            break
        print("Resposta inválida! Digite 's' para Sim ou 'n' para Não.")
    while True:
        retorno = input("Esse gasto terá retorno? (s/n): ").strip().lower()
        if retorno in ('s', 'n'):
            retorno_valor = float(input("Valor esperado de retorno (R$): ")) if retorno == 's' else 0
            break
        print("Resposta inválida! Digite 's' para Sim ou 'n' para Não.")
    if mes not in gastos:
        gastos[mes] = []
    gastos[mes].append({"descricao": descricao, "valor": valor, "fixo": fixo, "retorno": retorno_valor})
    salvar_gastos()
    print("✅ Gasto adicionado com sucesso!")

def remover_gasto(mes):
    visualizar_gastos(mes)
    if mes not in gastos or not gastos[mes]:
        return
    try:
        indice = int(input("Digite o número do gasto para remover: ")) - 1
        if 0 <= indice < len(gastos[mes]):
            del gastos[mes][indice]
            salvar_gastos()
            print("✅ Gasto removido com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida!")

def exibir_total(mes):
    total_gastos = sum(gasto["valor"] for gasto in gastos.get(mes, []))
    print(f"Total gasto no mês {mes}: R$ {total_gastos:.2f}")

def gerar_graficos(mes):
    if mes not in gastos or not gastos[mes]:
        print("Nenhum dado disponível para gerar gráficos.")
        return
    categorias = {}
    for gasto in gastos[mes]:
        categorias[gasto["descricao"]] = categorias.get(gasto["descricao"], 0) + gasto["valor"]
    labels = list(categorias.keys())
    valores = list(categorias.values())
    print("1 - Gráfico de Pizza")
    print("2 - Gráfico de Barras")
    opcao = input("Escolha o tipo de gráfico: ")
    if opcao == "1":
        plt.figure(figsize=(6,6))
        plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f"Distribuição de Gastos - {mes}")
        plt.show()
    elif opcao == "2":
        plt.figure(figsize=(8,6))
        plt.bar(labels, valores, color='blue')
        plt.xlabel("Categorias")
        plt.ylabel("Valor Gasto (R$)")
        plt.title(f"Gastos por Categoria - {mes}")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("Opção inválida!")

def exibir_menu(mes):
    saldo_disponivel = calcular_saldo_disponivel(mes)
    mes_numero, ano = mes.split("-")
    mes_nome = calendar.month_name[int(mes_numero)].capitalize()
    print(f"\n-------- Controle de Gastos ({mes_nome} {ano}) --------")
    print(f"Saldo disponível: R$ {saldo_disponivel:.2f}")
    print("1 - Adicionar gasto")
    print("2 - Visualizar gastos")
    print("3 - Exibir total gasto")
    print("4 - Definir renda mensal")
    print("5 - Gerar gráficos")
    print("6 - Remover gasto")
    print("7 - Mudar de mês")
    print("8 - Sair")

carregar_gastos()
if renda_mensal == 0:
    definir_renda_mensal()
while True:
    mes_atual = input("Digite o mês para gerenciar (ex: 03-2025): ")
    if re.fullmatch(r"(0[1-9]|1[0-2])-[0-9]{4}", mes_atual):
        break
    print("Formato inválido! Digite no formato MM-AAAA.")
while True:
    try:
        exibir_menu(mes_atual)
        opcao = int(input(": "))
        if opcao == 8:
            print("Saindo do programa...")
            break
        elif opcao == 7:
            mes_atual = input("Digite o novo mês (ex: 04-2025): ")
        elif opcao == 6:
            remover_gasto(mes_atual)
        elif opcao == 5:
            gerar_graficos(mes_atual)
        elif opcao == 4:
            definir_renda_mensal()
        elif opcao == 3:
            exibir_total(mes_atual)
        elif opcao == 2:
            visualizar_gastos(mes_atual)
        elif opcao == 1:
            adicionar_gasto(mes_atual)
        else:
            print("Opção inválida!")
    except ValueError:
        print("Digite um número válido!")
