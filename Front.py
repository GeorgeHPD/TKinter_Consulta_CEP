from tkinter import *
from tkinter import ttk
import time;
from PIL import ImageTk,Image

class Front():

    x_pad  =  5
    y_pad  =  3
    width_entry = 30
    
    #Janela
    
    window =  Tk()
    window.wm_title("Consulta CEP")
    window.configure(background="black")
    window.iconbitmap('py.ico')
    window.geometry("1300x500")
    localtime=time.asctime(time.localtime(time.time()))

    #Variaveis

    txt1    = StringVar()
    txt2    = StringVar()
    txt3    = StringVar()
    txt4    = StringVar()
    txt6    = StringVar()

    #Label

    lbl1    = Label(window, text="CEP", width=15)
    lbl2    = Label(window, text="Valor", width=15)
    lbl3    = Label(window, text="Região", width=15)
    lbl4    = Label(window, text="Risco", width=15)
    lbl5    = Label(window, text=localtime, width=50)
    lbl6    = Label(window, text="© 2019 George Luiz. Todos os direitos reservados.", width=50)

    ent1    = Entry(window, textvariable=txt1)
    ent2    = Entry(window, textvariable=txt2)
    ent3    = Entry(window, textvariable=txt3)
    ent4    = Entry(window, textvariable=txt4)

    listCEP     = Listbox(window, width=50)
    scrollCEP   = Scrollbar(window)

    btnViewAll      = ttk.Button(window, text="Ver todos")
    btnBuscar       = ttk.Button(window, text="Buscar")
    btnInserir      = ttk.Button(window, text="Inserir")
    btnUpdate       = ttk.Button(window, text="Atualizar Selecionado")
    btnDel          = ttk.Button(window, text="Deletar Selecionado")
    btnClose        = ttk.Button(window, text="Fechar")

    #GRID

    lbl1.grid(row=0, column=0)
    lbl2.grid(row=1, column=0)
    lbl3.grid(row=2, column=0)
    lbl4.grid(row=3, column=0)
		
	
    ent1.grid(row=0, column=1, padx=50, pady=50)
    ent2.grid(row=1, column=1)
    ent3.grid(row=2, column=1)
    ent4.grid(row=3, column=1)
    
    listCEP.grid(row=0, column=2, rowspan=10)
    scrollCEP.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    listCEP.configure(yscrollcommand=scrollCEP.set)
    scrollCEP.configure(command=listCEP.yview)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Front.window.mainloop()


