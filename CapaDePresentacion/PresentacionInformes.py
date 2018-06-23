from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.PresentacionPartidos import PresentacionPartidos
from tkinter import *
from tkinter import ttk


class PresentacionInformes:

    def mostrarPartidos(self):
        partido = PresentacionPartidos()
        vp, tree = partido.treePartidos()

        botonInforme=Button(vp, text="Ver Informe", command= lambda: self.seleccionPartido(tree))
        botonInforme.grid(column=1, row=0, sticky=S)


    def seleccionPartido(self, tree):
        partido = PresentacionPartidos()
        idPartido = partido.getIdPartido(tree)
        self.mostrarInforme(idPartido)


    def mostrarInforme(self, idPartido):
        cdn= CapaDeNegocio()
        arregloAsientosPartido = cdn.listarAsientosPartido(idPartido)

        tl=Toplevel()
        tree = ttk.Treeview(tl)
        tl.title("Asientos del partido")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        tree["column"]=("estado")
        tree.column("#0", width=100)
        tree.column("estado", width=100)
        tree.heading("#0", text="Número de Asiento")
        tree.heading("estado", text="Estado")

        for i in range(len(arregloAsientosPartido)):
            if arregloAsientosPartido[i][1] == 0:
                estado = "Vendido"
            else:
                estado= "Desocupado"
            tree.insert("", i,text=arregloAsientosPartido[i][0], values=(estado))

        tree.grid(column=0, row=0, columnspan=1000, sticky=N+E+S+W)







