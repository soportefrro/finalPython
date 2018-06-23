from tkinter import *
from tkinter import ttk
from CapaDePresentacion.PresentacionPartidos import *
from CapaDePresentacion.PresentacionInformes import *

class PresentacionInicio:
    def __init__(self):
        self.root= Tk()
        self.cdn=CapaDeNegocio()

    def inicio(self):

        botonVenta=Button(self.root, text="Venta Entradas", command=self.ventaEntradas)
        botonVenta.grid(column=1, row=0)

        botonInforme=Button(self.root, text="Informe Partido", command=self.informe)
        botonInforme.grid(column=2, row=0)

        self.root.mainloop()


    def ventaEntradas(self):
        partido=PresentacionPartidos()
        partido.mostrarPartidos()


    def informe(self):
        informe=PresentacionInformes()
        informe.mostrarPartidos()




