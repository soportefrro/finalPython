from CapaDeDatos.CDD_Entradas import CDD_Entradas
from CapaDeDatos.CDD_Partidos import *
from CapaDeDatos.CDD_Clientes import *

class CapaDeNegocio():

    def listarPartidos(self):
        self.cdd = CDD_Partidos()
        return self.cdd.listarPartidos()

    def listarAsientos(self, id):
        self.cdd = CDD_Partidos()
        return self.cdd.listarAsientos(id)

    def buscarCliente(self, dni):
        self.cdd=CDD_Clientes()
        return self.cdd.buscarCliente(dni)

    def buscarPartido(self, idPartido):
        self.cdd = CDD_Partidos()
        return self.cdd.buscarPartido(idPartido)

    def registrarCompra(self, nuevaEntrada):
        self.cdd = CDD_Entradas()
        self.cdd.registrarCompra(nuevaEntrada)



        
