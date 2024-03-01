import random
import tkinter

from tkinter import *
from tkinter import ttk

def tentar(*args):
    global tentativas
    tentativas += 1
    if int(palpite.get()) < numeroSorteado:
        mensagem.set("ERRROUUU...Muito pequeno seu palpite.")
    elif int(palpite.get()) > numeroSorteado:
        mensagem.set("ERRROUUU...Muito grande seu palpite.")
    else:
        mensagem.set(f"PARABÉNS! Acertou após {tentativas} tentativa(s)")

def entry_focus_in(event):
    palpite.set("")
    mensagem.set("")

tentativas = 0
numeroSorteado = random.randint(1, 100)
print(numeroSorteado)

janela = Tk()
janela.title("Adivinhe o número!")
janela.resizable(False, False)

frame = ttk.Frame(janela, padding="20 20 20 20")
frame.grid()

estilo = ttk.Style()
estilo.configure('my.TButton', font=('Arial', 18))

palpite = StringVar()
mensagem = StringVar()

label1 = ttk.Label(frame, padding="10 10 10 10", font=("Arial", 18))
label1['text'] = "Pensei em um número de 1 a 100! Tente adivinhar"
label1.grid(column=0, row=0, columnspan=3, sticky=(N, E, S, W))

label2 = ttk.Label(frame, padding="10 10 10 10", font=("Arial", 18))
label2['text'] = "Seu palpite: "
label2.grid(column=0, row=1, sticky=(N, E))

entrada = ttk.Entry(frame, width=10, textvariable=palpite, font=("Arial", 18))
entrada.grid(column=1, row=1, padx=10, sticky=(N, W))

botao = ttk.Button(frame, padding="10 10 10 10", text="Tentar", style='my.TButton', command=tentar)
botao.grid(column=2, row=1)

resposta = ttk.Label(frame, padding="10 10 10 10", textvariable=mensagem, font=("Arial", 18))
resposta.grid(column=0, row=3, columnspan=3, sticky=(N, E, S, W))

entrada.focus()

janela.bind("<Return>", tentar)
entrada.bind("<FocusIn>", entry_focus_in)

janela.mainloop()