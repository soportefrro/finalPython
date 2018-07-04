from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.PresentacionPartidos import PresentacionPartidos
from tkinter import *
from tkinter import ttk


class PresentacionInformes:

    def mostrarPartidos(self):
        partido = PresentacionPartidos()
        vp, tree = partido.treePartidos()

        botonInforme=Button(vp, text="Ver Informe", command= lambda: self.seleccionPartido(tree))
        botonInforme.grid(column=1, row=5, sticky=S)


    def seleccionPartido(self, tree):
        partido = PresentacionPartidos()
        idPartido = partido.getIdPartido(tree)
        self.mostrarInforme(idPartido)


    def mostrarInforme(self, idPartido):
        cdn= CapaDeNegocio()
        entradasVendidas = cdn.buscarEntradasParaPartido(idPartido)

        tl=Toplevel()
        tree = ttk.Treeview(tl)
        tl.title("Asientos del partido")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        tree["column"]=("fechaventa", "nombreCliente", "apellidoCliente", "precio")
        tree.column("#0", width=100)
        tree.column("fechaventa", width=100)
        tree.column("nombreCliente", width=100)
        tree.column("apellidoCliente", width=100)
        tree.column("precio", width=100)
        tree.heading("#0", text="Número de Asiento")
        tree.heading("fechaventa", text="Fecha de Venta")
        tree.heading("nombreCliente", text="Nombre Cliente")
        tree.heading("apellidoCliente", text="Apellido Cliente")
        tree.heading("precio", text="Importe Abonado")


        for i in entradasVendidas:
            #print("id del partido obje" +partido.idPartido)
            #print("id del partido de la entrada" + i.partido.idPartido)
            importe = i.partido.precioUSD * i.cotizacionVenta
            tree.insert("", i,text= i.nroAsiento, values=(i.fechaVenta, i.cliente.nombre, i.cliente.apellido, importe))
            sumatoria =+ importe



        tree.grid(column=0, row=0, columnspan=1000, sticky=N+E+S+W)

        totalRecaudado=Label(vp, text="Total Recaudado: {0}".format(sumatoria))
        totalRecaudado.grid(column=0, row=1000, sticky=E+S)







