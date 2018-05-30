from tkinter import *
from tkinter import ttk
from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.SeleccionAsiento import *


class Inicio():
    def __init__(self):
        self.root= Tk()
        self.cdn=CapaDeNegocio()
        self.tree = ttk.Treeview(self.root)


    def inicializacion(self):
        vp=Frame(self.root)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        self.tree["column"]=("pais1", "pais2","instancia", "precio")
        self.tree.column("#0", width=100)
        self.tree.column("pais1", width=100)
        self.tree.column("pais2", width=100)
        self.tree.column("instancia", width=100)
        self.tree.column("precio", width=100)
        self.tree.heading("#0", text="Fecha")
        self.tree.heading("pais1", text="Selección 1")
        self.tree.heading("pais2", text="Selección 2")
        self.tree.heading("instancia", text="Instancia")
        self.tree.heading("precio", text="Precio(USD)")

        listaPartidos= self.cdn.listarPartidos()

        for i in range(len(listaPartidos)):
              self.tree.insert("", i,text=listaPartidos[i][1], values=(listaPartidos[i][2],listaPartidos[i][3],listaPartidos[i][4],listaPartidos[i][5],listaPartidos[i][0]))


        botonSeleccionar = Button(self.root, text="Seleccionar", command= self.seleccionarAsiento)
        botonSeleccionar.grid(column=1, row=1, sticky=S)


        self.tree.grid(column=0, row=0, columnspan=1000, sticky=N+E+S+W)
        self.root.mainloop()




    def seleccionarAsiento(self):
        posicion= self.tree.selection()
        partidoSeleccionado = self.tree.item(posicion)
        idPartido=partidoSeleccionado["values"][4]
        asientos= SeleccionAsiento()
        asientos.seleccionarAsiento(idPartido)
