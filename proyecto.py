import random
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Datos')
window.config(padx=5, pady= 5)
time = 0
tfont = {
    'fontname': 'Comic Sans MS', 
    'size': 18
}

lfont = {
    'fontname': 'Franklin Gothic Medium',
    'size': 12
}


def dado_tirado(nd: int, a: int) -> dict:
    info = {}
    times = int(entryd.get()) + 1
    while times > 0:
        times-=1
        for i in range(0, a):
            number = random.randint(1, 6)
            if number != 1:
                info[f"{i}"] = number
            else:
                info[f"{i}"] = 0
    else:
        return info

def check(info: dict) -> dict:
    for e in info:
        if 0 in info[f"{e}"]:
             for i in range(info[f"{e}"].index(0), len(info[f"{e}"])):
                info[f"{e}"][i] = 0
    return info

def okey():
    try:
        global time
        time += 1
        y = []
        vd = int(entryd.get())
        nd = int(entryI.get())
        if vd > nd:
            a = nd+vd-nd
        else:
            a = nd-(nd-vd)

        veces = [str(e) for e in range(0, vd)]

        new_info = {
            "Dado": veces,
        }

        for i in range(0, nd):
            new_info[f"Try {i}"] = [dado_tirado(nd, a)[o] for o in dado_tirado(nd, a)]

        csv = pd.DataFrame(check(new_info))
        csv.to_csv("dado.csv", index=False)

        for i in range(0, len(new_info)-1):
            y.append(sum(new_info[f"Try {i}"]))

        if time != 1: 
            plt.clf()
        y.sort(reverse=True)
        plt.figure("Proyecto")
        plt.xlabel("Turno", **lfont)
        plt.ylabel("Dados Sin Decaer", **lfont)
        plt.title("Decaimiento Radiactivo", **tfont)
        plt.plot(range(0, nd), y, color='black', marker='o', markerfacecolor = 'r', label='N = N_0e^(-λt)')
        plt.legend()
        plt.grid(linestyle=':')
        plt.show()
    except ValueError:
        messagebox.showerror(title="ERROR", message="Enter a Valid Number")

def okeyf(event):
    okey()

NumeroD = Label(text='Número De Dados: ', font=('Tekton Pro', 10))
NumeroD.grid(column=0, row=0)

intentos = Label(text='Veces que se lanzaran los dados: ', font=('Tekton Pro', 10))
intentos.grid(column=0, row=1)

entryd = Entry(width=15, borderwidth=3)
entryd.grid(column=1, row=0, pady=3)
entryd.focus()

entryI = Entry(width=15, borderwidth=3)
entryI.grid(column=1, row=1, pady=3)

ok_button = Button(text="Ok", width=30, borderwidth=3, command=okey, bg='gray89')
ok_button.grid(column=0, row=2, columnspan=2, pady=3)

window.bind("<Return>", okeyf)
window.mainloop()