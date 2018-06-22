from tkinter import *
from tkinter import ttk
from CapaDeNegocio.CapaDeNegocio import *
from CapaDePresentacion.PresentacionAsientos import *
import requests


class PresentacionPartidos():
    def __init__(self):
        self.root= Tk()
        self.cdn=CapaDeNegocio()
        self.tree = ttk.Treeview(self.root)


    def mostrarPartidos(self):
        vp=Frame(self.root)
        vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))

        self.tree["column"]=("pais1", "pais2","instancia", "precio", "precioARS")
        self.tree.column("#0", width=100)
        self.tree.column("pais1", width=100)
        self.tree.column("pais2", width=100)
        self.tree.column("instancia", width=100)
        self.tree.column("precio", width=100)
        self.tree.column("precioARS", width = 100)
        self.tree.heading("#0", text="Fecha")
        self.tree.heading("pais1", text="Selección 1")
        self.tree.heading("pais2", text="Selección 2")
        self.tree.heading("instancia", text="Instancia")
        self.tree.heading("precio", text="Precio(USD)")
        self.tree.heading("precioARS", text="Precio(ARS)")

        listaPartidos= self.cdn.listarPartidos()

        #API DOLAR (Esto en la de negocio)
        url_dolar = "http://ws.geeklab.com.ar/dolar/get-dolar-json.php"
        json_dolar = requests.get(url_dolar).json()
        cotizacion_dolar = float(json_dolar["libre"])


        for i in range(len(listaPartidos)):
            precio_dolares = int(float(listaPartidos[i][5]) * cotizacion_dolar)

            self.tree.insert("", i,text=listaPartidos[i][1], values=(listaPartidos[i][2],listaPartidos[i][3],listaPartidos[i][4],listaPartidos[i][5], precio_dolares,  listaPartidos[i][0] ))

        botonSeleccionar = Button(self.root, text="Seleccionar", command= self.seleccionarPartido)
        botonSeleccionar.grid(column=1, row=1, sticky=S)


        self.tree.grid(column=0, row=0, columnspan=1000, sticky=N+E+S+W)
        self.root.mainloop()




    def seleccionarPartido(self):
        posicion = self.tree.selection()
        if len(posicion) == 1:
            partidoSeleccionado = self.tree.item(posicion)
            idPartido = partidoSeleccionado["values"][5]
            asientos = PresentacionAsientos()
            asientos.listarAsientos(idPartido)
        else:
            tl=Toplevel()
            tl.title("Error")
            vp=Frame(tl)
            vp.grid(column=0, row=0, padx=(100,100), pady=(20,20), sticky=(N, S, E, W))
            etique=Label(vp, text="Por favor, seleccione un partido")
            etique.grid(column=1, row=1)
            botoncerrar=Button(vp, text="Aceptar", command=tl.destroy)
            botoncerrar.grid(column=1, row=2)

