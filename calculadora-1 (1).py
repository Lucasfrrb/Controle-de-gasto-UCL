from tkinter import *
from tkinter import messagebox

'''Esstrutura da Janela'''

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("475x470")
calculadora.resizable(False, False)
calculadora.config(bg="gray") 


'''Funcoes'''

def BTNumeros(numero):
    PegaNumero = CampoNumeros.get()
    CampoNumeros.delete(0, END)
    CampoNumeros.insert(0, str(PegaNumero) + str(numero))
    return
def soma():
    PegaNumero = CampoNumeros.get()
    global PrimeiroNumero
    global operacao
    operacao = 'soma'
    PrimeiroNumero = float(PegaNumero)
    CampoNumeros.delete(0, END)
    return
def subtracao():
    PegaNumero = CampoNumeros.get()
    global PrimeiroNumero
    global operacao
    operacao = 'subtracao'
    PrimeiroNumero = float(PegaNumero)
    CampoNumeros.delete(0, END)
    return
def multiplicacao():
    PegaNumero = CampoNumeros.get()
    global PrimeiroNumero
    global operacao
    operacao = 'multiplicacao'
    PrimeiroNumero = float(PegaNumero)
    CampoNumeros.delete(0, END)
    return
def divisao():
    PegaNumero = CampoNumeros.get()
    global PrimeiroNumero
    global operacao
    operacao = 'divisao'
    PrimeiroNumero = float(PegaNumero)
    CampoNumeros.delete(0, END)
    return
def porcentagem():
    PegaNumero = CampoNumeros.get()
    global PrimeiroNumero
    global operacao
    operacao = 'porcentagem'
    PrimeiroNumero = float(PegaNumero)
    CampoNumeros.delete(0, END)
    return
def potencia():
    PegaNumero = CampoNumeros.get()
    global PrimeiroNumero
    global operacao
    operacao = 'potencia'
    PrimeiroNumero = float(PegaNumero)
    CampoNumeros.delete(0, END)
    return
def raiz():
    PegaNumero = CampoNumeros.get()
    global PrimeiroNumero
    global operacao
    operacao = 'raiz'
    PrimeiroNumero = float(PegaNumero)
    CampoNumeros.delete(0, END)
    return
def igual():
    PegaNumero = CampoNumeros.get()
    CampoNumeros.delete(0, END)
    if operacao == 'soma':
          CampoNumeros.insert(0, PrimeiroNumero + float(PegaNumero))
    elif operacao == 'subtracao':
         CampoNumeros.insert(0, PrimeiroNumero - float(PegaNumero))
    elif operacao == 'multiplicacao':
         CampoNumeros.insert(0, PrimeiroNumero * float(PegaNumero))
    elif operacao == 'divisao':
         CampoNumeros.insert(0, PrimeiroNumero / float(PegaNumero))
    elif operacao == 'porcentagem':
         CampoNumeros.insert(0, (PrimeiroNumero * float(PegaNumero)) / 100)
    elif operacao == 'potencia':
         CampoNumeros.insert(0, PrimeiroNumero ** float(PegaNumero))
    elif operacao == 'raiz':
         CampoNumeros.insert(0, PrimeiroNumero ** 0.5)
    return
           

'''Entry'''

CampoNumeros = Entry(calculadora, width = 50)   
CampoNumeros.place(x=100, y=25)
CampoNumeros.focus_set()
CampoNumeros.config(bg = "black", fg = "white", relief = FLAT)
CampoNumeros.config(justify = "left")
CampoNumeros.config(highlightbackground = "black")
CampoNumeros.config(highlightcolor = "black")
CampoNumeros.config(highlightthickness = 0)

'''Botoes'''

BT1 = Button(calculadora, text = 1, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(1))
BT1.place(x=50, y=150)

BT2 = Button(calculadora, text = 2, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(2))
BT2.place(x=150, y=150)

BT3 = Button(calculadora, text = 3, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(3))
BT3.place(x=250, y=150)

BT4 = Button(calculadora, text = 4, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(4))
BT4.place(x=50, y=225)

BT5 = Button(calculadora, text = 5, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(5))
BT5.place(x=150, y=225)

BT6 = Button(calculadora, text = 6, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(6))
BT6.place(x=250, y=225)

BT7 = Button(calculadora, text = 7, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(7))
BT7.place(x=50, y=300)

BT8 = Button(calculadora, text = 8, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(8))
BT8.place(x=150, y=300)

BT9 = Button(calculadora, text = 9, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(9))
BT9.place(x=250, y=300)

BT0 = Button(calculadora, text = 0, relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros(0))
BT0.place(x=150, y=375)

BTPonto = Button(calculadora, text = ".", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: BTNumeros('.'))
BTPonto.place(x=50, y=375)

BTIgual = Button(calculadora, text = "=", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = igual)
BTIgual.place(x=250, y=375)

BTDivisao = Button(calculadora, text = "/", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = divisao)
BTDivisao.place(x=350, y=150)

BTMultiplicacao = Button(calculadora, text = "*", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = multiplicacao)
BTMultiplicacao.place(x=350, y=225)

BTSoma = Button(calculadora, text = "+", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = soma)
BTSoma.place(x=350, y=300)

BTSubtracao = Button(calculadora, text = "-", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = subtracao)
BTSubtracao.place(x=350, y=375)

BTC = Button(calculadora, text = "C", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = lambda: CampoNumeros.delete(0, END))
BTC.place(x=50, y=75)

BTPorcentagem = Button(calculadora, text = "%", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = porcentagem)
BTPorcentagem.place(x=150, y=75)

BTPotencia = Button(calculadora, text = "x²", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = potencia)
BTPotencia.place(x=250, y=75)

BTRaiz = Button(calculadora, text = "√", relief = FLAT, width = 10, height = 3, bg = "black", fg = "white", command = raiz)
BTRaiz.place(x=350, y=75)




calculadora.mainloop()