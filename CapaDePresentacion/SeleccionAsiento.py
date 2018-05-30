from tkinter import *
from tkinter import ttk

from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.DatosCliente import DatosCliente


class SeleccionAsiento():
    def __init__(self):
        self.tl=Toplevel()
        self.tree = ttk.Treeview(self.tl)
    def seleccionarAsiento(self, idPartido):

        self.tl.title("Elegir asientos")


        vp=Frame(self.tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        self.tree["column"]=("estado")
        self.tree.column("#0", width=100)
        self.tree.column("estado", width=100)
        self.tree.heading("#0", text="Número de Asiento")
        self.tree.heading("estado", text="Estado")

        cdn= CapaDeNegocio()
        arregloAsientos = cdn.listarAsientos(idPartido)


        for i in range(len(arregloAsientos)):
            if arregloAsientos[i][1]:
                estadoAsiento="Libre"
            else: estadoAsiento= "Ocupado"
            self.tree.insert("", i,text=arregloAsientos[i][0], values=(estadoAsiento))

        botonSiguiente = Button(self.tl, text="Siguiente", command=lambda: self.solicitarDatosCliente(idPartido))
        botonSiguiente.grid(column=1, row=1, sticky=S)



        self.tree.grid(column=0, row=0, columnspan=1000, sticky=N+E+S+W)
        self.tl.mainloop()


    def solicitarDatosCliente(self, idPartido):
        posicion= self.tree.selection()
        asientoSeleccionado = self.tree.item(posicion)
        idAsiento = asientoSeleccionado["text"]
        dc = DatosCliente(idPartido, idAsiento)
        dc.busquedaRegistro()  #capaz que tenemos que agregar el IdAsiento
