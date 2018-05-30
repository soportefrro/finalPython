from tkinter import *
from tkinter import ttk
from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.Compra import Compra


class DatosCliente:

    def __init__(self, idPartido, idAsiento):
        self.idPartido = idPartido
        self.idAsiento = idAsiento

    def busquedaRegistro(self):
        tl=Toplevel()
        tl.title("Buscar Cliente")
        tree = ttk.Treeview(tl)

        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        self.dni=StringVar()

        etiquetadni=Label(vp, text= "DNI: ")
        etiquetadni.grid(column=0, row=0)
        entradadni=Entry(vp, width= 20, textvariable= self.dni)
        entradadni.grid(column=1, row=0)

        botonBuscar = Button(vp, text = "Buscar Cliente", command= lambda : self.buscar())
        botonBuscar.grid(column = 1, row = 3)


    def buscar(self):
        #Ventana de Confirmacion de datos de cliente
        tl=Toplevel()
        tl.title("Datos del Cliente")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        dni=self.dni.get()
        cdn=CapaDeNegocio()
        cliente= cdn.buscarCliente(dni) #objeto cliente

        self.nombre = StringVar()
        self.dni = StringVar()
        self.apellido = StringVar()
        self.mail = StringVar()
        self.nombre.set(cliente.nombre)
        self.dni.set(int(cliente.dni))
        self.apellido.set(cliente.apellido)
        self.mail.set(cliente.mail)

        etiquetadni=Label(vp, text= "DNI: ")
        etiquetadni.grid(column=0, row=2)
        entradadni=Label(vp, width= 20, textvariable= self.dni)
        entradadni.grid(column=1, row=2)

        etiquetanombre=Label(vp, text= "Nombre: ")
        etiquetanombre.grid(column=0, row=0)
        entradanombre=Label(vp, width= 20, textvariable= self.nombre)
        entradanombre.grid(column=1, row=0)

        etiquetaapellido=Label(vp, text= "Apellido: ")
        etiquetaapellido.grid(column=0, row=1)
        entradaapellido=Label(vp, width= 20, textvariable= self.apellido)
        entradaapellido.grid(column=1, row=1)

        etiquetamail=Label(vp, text= "Mail: ")
        etiquetamail.grid(column=0, row=3)
        entradamail=Label(vp, width= 30, textvariable= self.mail)
        entradamail.grid(column=1, row=3)



        botonCancelar=Button(vp, text="Cancelar", command=tl.destroy)
        botonCancelar.grid(column=0, row=5)

        compra = Compra()

        botonComprar=Button(vp, text="Comprar", command=lambda:compra.confirmarCompra(cliente, self.idPartido, self.idAsiento ))
        botonComprar.grid(column=1, row=5)




