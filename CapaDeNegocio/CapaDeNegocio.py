from CapaDeDatos.CDD_Entradas import CDD_Entradas
from CapaDeDatos.CDD_Partidos import *
from CapaDeDatos.CDD_Clientes import *

class CapaDeNegocio():

    def listarPartidos(self):
        self.cdd = CDD_Partidos()
        return self.cdd.listarPartidos()

    def listarAsientosDisponibles(self, id):
        self.cdd = CDD_Partidos()
        asientos = self.cdd.listarAsientosDisponibles(id)
        if len(asientos) == 0:
            return False
        else: return asientos

    def buscarCliente(self, dni):
        if dni != "":
            self.cdd=CDD_Clientes()
            return self.cdd.buscarCliente(dni)
        else: return False

    def buscarPartido(self, idPartido):
        self.cdd = CDD_Partidos()
        return self.cdd.buscarPartido(idPartido)

    def registrarCompra(self, nuevaEntrada):
        self.cdd = CDD_Entradas()
        self.cdd.registrarCompra(nuevaEntrada)


    def altaCliente(self, cliente):
        self.cdd = CDD_Clientes()
        if self.cdd.contarClientesPorDni(cliente.dni) == 0 and cliente.dni.isdigit() and cliente.dni != "" and cliente.apellido != "" and cliente.nombre != "" and cliente.mail != "":
            self.cdd.altaCliente(cliente)
            return True
        else: return False



        
