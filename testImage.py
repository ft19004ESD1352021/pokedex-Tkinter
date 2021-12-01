import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import customtkinter as ctk
from pandas.core import frame
import os



ventana = Tk()
ventana.title("HIJAs")

# Primer Frame
panel1 = tk.LabelFrame(ventana)
# Canvas
canvas = tk.Canvas(panel1, bg="white")
canvas.pack(side="top", fill="x", expand="yes")
# Ventanas dentro del frame
frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame, anchor=NW)
panel1.pack(fill="both", expand="yes", padx=0, pady=0)

for i in range(3):
    # Ver Boton
    # image Pokemon
    frm_test = tk.Frame(canvas, padx=1, pady=1, bg="white")
    frm_test.grid(row=i, column=0)
    try:
        imag = tk.PhotoImage(file='pokeicons/abra.png').zoom(2)
        imagen =tk.Button(master=frm_test,image=imag, bg="white", relief=FLAT).pack()
        #tk.Label()
    except:
        img_Poc = tk.Label(
            master=frm_test, text="Icon No Found", bg="white", relief=FLAT).pack()
    # Estadisticas
    # pokeNombre,pokeAtaque,pokeDefensa,pokeVida
    
    frm_test = tk.Frame(canvas, padx=1, pady=1, bg="white")
    frm_test.grid(row=i, column=1, pady=10, padx=10)

    tk.Label(master=frm_test, text="ATAQUE:",
             bg="white", fg="black").pack()
    barra = Progressbar(master=frm_test, orient=HORIZONTAL,
                        value=50, length=100, mode='indeterminate')
    barra.pack(expand=True)
    tk.Label(master=frm_test, text="DEFENSA:",
             bg="white", fg="black").pack()
    barra = Progressbar(master=frm_test, orient=HORIZONTAL,
                        value=50, length=100, mode='indeterminate')
    barra.pack(expand=True)
    tk.Label(master=frm_test, text="VIDA:", bg="white", fg="black").pack()
    barra = Progressbar(master=frm_test, orient=HORIZONTAL,
                        value=50, length=100, mode='indeterminate')
    barra.pack(expand=True)

    # Valor Total
    frm_test = tk.Frame(canvas, padx=1, pady=1, bg="white", relief=FLAT)
    frm_test.grid(row=i, column=2, pady=10, padx=10)

    tk.Label(master=frm_test, text="PODER TOTAL:",
             bg="white", fg="black").pack()
    barra = Progressbar(master=frm_test, orient=HORIZONTAL,
                        value=50, length=100, mode='indeterminate')
    barra.pack(expand=True)
    
ventana.mainloop()


