from tkinter import *
from tkinter import ttk

from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.PresentacionCliente import PresentacionCliente


class PresentacionAsientos():

    def listarAsientos(self, idPartido):

        cdn= CapaDeNegocio()
        arregloAsientos = cdn.listarAsientosDisponibles(idPartido)

        if not arregloAsientos:
            tl=Toplevel()
            tl.title("No hay disponibilidad")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            msjNoDisp=Label(vp, text="No hay asientos disponibles")
            msjNoDisp.grid(column=0, row=0)
        else:
            self.tl=Toplevel()
            self.tree = ttk.Treeview(self.tl)
            self.tl.title("Elegir asientos")
            vp=Frame(self.tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

            self.tree["column"]=("estado")
            self.tree.column("#0", width=100)
            self.tree.column("estado", width=100)
            self.tree.heading("#0", text="Número de Asiento")
            self.tree.heading("estado", text="Estado")

            for i in range(len(arregloAsientos)):
                self.tree.insert("", i,text=arregloAsientos[i][0], values=("Libre"))

            botonSiguiente = Button(self.tl, text="Siguiente", command=lambda: self.seleccionarAsiento(idPartido))
            botonSiguiente.grid(column=1, row=1, sticky=S)
            self.tree.grid(column=0, row=0, columnspan=1000, sticky=N+E+S+W)

            self.tl.mainloop()

    def seleccionarAsiento(self, idPartido):
        posicion= self.tree.selection()
        if len(posicion) == 1:
            asientoSeleccionado = self.tree.item(posicion)
            idAsiento = asientoSeleccionado["text"]
            pc = PresentacionCliente(idPartido, idAsiento)
            pc.busquedaRegistro()

        else:
            tl=Toplevel()
            tl.title("Error")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="Por favor, seleccione un asiento")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
            botoncerrar.grid(column=1, row=2)
