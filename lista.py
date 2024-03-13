from tkinter import *
from tkinter import ttk
from tkinter import font

def adicionar(*args):
    global lista
    item_adicionado = item.get()
    if(item_adicionado != ""):
        lista.append(item_adicionado)
        listavar.set(lista)

def excluir(*args):
    selecionado = listbox.curselection()

janela = Tk()
janela.title("Lista Genérica de Itens")
janela.resizable(False, False) #Impede que redimensione a janela

frame = ttk.Frame(janela, padding="20 20 20 20")
frame.grid()

#criamos um estilo customizado para a fonte do botao
estilo = ttk.Style()
estilo.configure("my.TButton", font=("arial", 18))

item = StringVar()
entrada = ttk.Entry(frame, width=10, textvariable=item)
entrada["font"] = ("Arial", 10)
entrada.grid(column=0, row=0, sticky=(N, E))

botao = ttk.Button(frame, text="Adicionar", style="my.TButton")
botao["command"] = adicionar
botao.grid(column=1, row=0)

lista = ["c", "Java", "Python", "JavaScript"]
listavar = StringVar(value=lista)
listbox = Listbox(frame, height=10, listvariable=listavar)

#fonte listbox
fonte_list = font.Font(name="Arial", size=10)
listbox.config(font=fonte_list)

#adicionando barra de rolagem a lista
# scrollbar = Scrollbar(listbox, orient=VERTICAL)
# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
# scrollbar.grid(column=1, sticky=N+E)

listbox.grid(column=0, row=1)

botao_excluir = ttk.Button(frame, text="Excluir")
botao_excluir["command"] = excluir
botao_excluir["style"] = "my.TButton"
botao_excluir.grid(column=1, row=1)


janela.mainloop()