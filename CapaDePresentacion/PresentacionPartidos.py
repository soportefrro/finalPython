from tkinter import *
from tkinter import ttk
from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.PresentacionAsientos import *



class PresentacionPartidos():
    def __init__(self):
        self.cdn=CapaDeNegocio()


    def mostrarPartidos(self):
        vp, tree = self.treePartidos()
        botonSeleccionar = Button(vp, text="Seleccionar", command= lambda: self.seleccionarPartido(tree))
        botonSeleccionar.grid(column=1, row=1, sticky=S)

    def getIdPartido(self, arbol): #gugu: me genera duda si este método no tendría que estar en CdN
        posicion = arbol.selection()
        if len(posicion) == 1:
            partidoSeleccionado = arbol.item(posicion)
            idPartido = partidoSeleccionado["values"][5]
            return idPartido
        else:
            tl=Toplevel()
            tl.title("Error")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="Por favor, seleccione un partido.")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
            botoncerrar.grid(column=1, row=2)
            return False



    def seleccionarPartido(self, tree):
        idPartido = self.getIdPartido(tree)
        #valido que el usuario haya elegido un partido
        if idPartido:
            asientos = PresentacionAsientos()
            asientos.listarAsientos(idPartido)


    def treePartidos(self):
        tl=Toplevel()
        tl.title("Partidos")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        self.tree = ttk.Treeview(vp)

        self.tree["column"]=("pais1", "pais2","instancia", "precioUSD", "precioARS")
        self.tree.column("#0", width=100)
        self.tree.column("pais1", width=100)
        self.tree.column("pais2", width=100)
        self.tree.column("instancia", width=100)
        self.tree.column("precioUSD", width=100)
        self.tree.column("precioARS", width = 100)
        self.tree.heading("#0", text="Fecha")
        self.tree.heading("pais1", text="Selección 1")
        self.tree.heading("pais2", text="Selección 2")
        self.tree.heading("instancia", text="Instancia")
        self.tree.heading("precioUSD", text="Precio(USD)")
        self.tree.heading("precioARS", text="Precio(ARS)")

        listaPartidos= self.cdn.listarPartidos()

        for i in listaPartidos:
            self.tree.insert("", i.idPartido, text=i.fecha, values=(i.pais1, i.pais2, i.instancia, "%.2f" % i.precioUSD, "%.2f" % i.precioARS, i.idPartido))

        self.tree.grid(column=0, row=0, columnspan=1000, sticky=N+E+S+W)

        return vp, self.tree


