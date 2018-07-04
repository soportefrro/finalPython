from datetime import date
from CapaDeNegocio.CapaDeNegocio import CapaDeNegocio
from Entrada import Entrada
from tkinter import *
from GenerarHTML import GenerarHTML


class PresentacionCompra():

    def confirmarCompra(self, cliente, idPartido, idAsiento):
        cdn = CapaDeNegocio()
        partido = cdn.buscarPartido(idPartido)
        cotizacionVenta = cdn.obtenerCotizacionDolar()
        nuevaEntrada = Entrada(0, cliente, partido, date.today().strftime('%Y%m%d'), idAsiento, cotizacionVenta, partido.precioUSD, partido.precioARS) #instancio una nueva entrada

        cdn.registrarCompra(nuevaEntrada)

        generadorhtml = GenerarHTML()
        generadorhtml.generarHTMLEntrada(nuevaEntrada)

        tl=Toplevel()
        tl.title("Comprobante de Compra")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
        separador = Label(vp, text="-------------------------------------------------------------")
        etique=Label(vp, text="Comprobante de Compra", fg="black", bg="white")
        etique.grid(column=1, row=1)
        compr=Label(vp, text="Numero de Comprobante: " + str(nuevaEntrada.nroComprobante))
        compr.grid(column=1, row = 2)
        separador.grid(column=1, row=3)
        datosCliente=Label(vp, text="DATOS DEL CLIENTE\nNombre y apellido: " + cliente.nombre + " " + cliente.apellido + "\nDNI: " + cliente.dni)
        datosCliente.grid(column=1, row=4)
        separador.grid(column=1, row=5)
        datosPartido=Label(vp, text="Partido: " + partido.pais1 + " vs " + partido.pais2 + "\t Fecha: " + str(partido.fecha) + "\nEstadio: " + partido.estadio + "\t Instancia: " + partido.instancia)
        datosPartido.grid(column=1, row=6, sticky=W)
        datosAsiento = Label(vp, text="Asiento Nro.: " + str(nuevaEntrada.nroAsiento))
        datosAsiento.grid(column=1, row=7, sticky=W)
        botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
        botoncerrar.grid(column=1, row=8)

