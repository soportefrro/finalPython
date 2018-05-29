from tkinter import *
from CapaDeNegocio.CapaDeNegocio import *


class SeleccionAsiento():
    def seleccionarAsiento(self, fecha, pais1, pais2):
        tl=Toplevel()
        tl.title("Elegir asientos")

        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        cdn= CapaDeNegocio()

