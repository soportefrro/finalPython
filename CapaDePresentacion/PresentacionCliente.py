from tkinter import *
from tkinter import ttk
from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.PresentacionCompra import PresentacionCompra


class PresentacionCliente:

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

        botonBuscar = Button(vp, text = "Buscar Cliente", command= lambda : self.leerCampoDNI())
        botonBuscar.grid(column = 1, row = 3)

        botonRegistrar = Button(vp, text = "Registrar Cliente", command= lambda : self.datosRegistro())
        botonRegistrar.grid(column = 2, row = 3)


    def leerCampoDNI(self):
        dni=self.dni.get()
        self.buscar(dni)

    def buscar(self, dni):

        cdn=CapaDeNegocio()
        cliente= cdn.buscarCliente(dni) #objeto cliente

        if cliente:
            #Ventana de Confirmacion de datos de cliente
            tl=Toplevel()
            tl.title("Datos del Cliente")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
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

            compra = PresentacionCompra()

            botonComprar=Button(vp, text="Comprar", command=lambda:compra.confirmarCompra(cliente, self.idPartido, self.idAsiento ))
            botonComprar.grid(column=1, row=5)

        else:
            # ventana de confirmación
            tl=Toplevel()
            tl.title("Error")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="Cliente no encontrado.")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
            botoncerrar.grid(column=1, row=2)

    def datosRegistro(self):
        self.nombre=StringVar()
        self.dni=StringVar()
        self.apellido= StringVar()
        self.mail = StringVar()

        #Ventana de Registro de datos de cliente
        tl=Toplevel()
        tl.title("Registro del Cliente")
        vp=Frame(tl)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        etiquetadni=Label(vp, text= "DNI: ")
        etiquetadni.grid(column=0, row=2)
        entradadni=Entry(vp, width= 20, textvariable= self.dni)
        entradadni.grid(column=1, row=2)

        etiquetanombre=Label(vp, text= "Nombre: ")
        etiquetanombre.grid(column=0, row=0)
        entradanombre=Entry(vp, width= 20, textvariable= self.nombre)
        entradanombre.grid(column=1, row=0)

        etiquetaapellido=Label(vp, text= "Apellido: ")
        etiquetaapellido.grid(column=0, row=1)
        entradaapellido=Entry(vp, width= 20, textvariable= self.apellido)
        entradaapellido.grid(column=1, row=1)

        etiquetamail=Label(vp, text= "Mail: ")
        etiquetamail.grid(column=0, row=3)
        entradamail=Entry(vp, width= 30, textvariable= self.mail)
        entradamail.grid(column=1, row=3)



        botonCancelar=Button(vp, text="Cancelar", command=tl.destroy)
        botonCancelar.grid(column=1, row=5)

        botonRegistrar=Button(vp, text="Registrar", command=lambda: self.registrar())
        botonRegistrar.grid(column=0, row=5)

    def registrar(self):
        nombre=self.nombre.get()
        apellido=self.apellido.get()
        dni=self.dni.get()
        mail=self.mail.get()

        #Instancia e inicializa el cliente
        cliente= Cliente(dni, nombre, apellido, mail)
        cdn=CapaDeNegocio()
        registro = cdn.altaCliente(cliente)

        if registro:

            # ventana de confirmación
            tl=Toplevel()
            tl.title("Cliente registrado")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="Cliente registrado con éxito.")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command= lambda:self.buscar(cliente.dni))
            botoncerrar.grid(column=1, row=2)

        else:
            # ventana de confirmación
            tl=Toplevel()
            tl.title("Error")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="Ha ocurrido un error.")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
            botoncerrar.grid(column=1, row=2)



