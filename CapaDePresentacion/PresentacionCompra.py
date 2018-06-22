from datetime import date
from CapaDeNegocio.CapaDeNegocio import CapaDeNegocio
from Entrada import Entrada
from tkinter import *


class PresentacionCompra():

    def confirmarCompra(self, cliente, idPartido, idAsiento):
        cdn = CapaDeNegocio()
        partido = cdn.buscarPartido(idPartido)
        nuevaEntrada = Entrada(0, cliente, partido, date.today().strftime('%Y%m%d') , idAsiento) #instancio una nueva entrada

        cdn.registrarCompra(nuevaEntrada)

        tl=Toplevel()
        tl.title("Comprobante de Compra")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
        etique=Label(vp, text="Comprobante de Compra")
        etique.grid(column=1, row=1)
        compr=Label(vp, text="Numero de Comprobante: " + str(nuevaEntrada.nroComprobante))
        compr.grid(column=1, row = 2)
        datosCliente=Label(vp, text=cliente.nombre + " " + cliente.apellido + " " + cliente.dni)
        datosCliente.grid(column=1, row=3)
        datosPartido=Label(vp, text=str(partido.fecha)+ " " + partido.estadio +" " + partido.instancia+ " " + partido.pais1 + " vs " + partido.pais2)
        datosPartido.grid(column=1, row=4)

        botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
        botoncerrar.grid(column=1, row=6)

