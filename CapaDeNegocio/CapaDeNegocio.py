from CapaDeDatos.CDD_Entradas import CDD_Entradas
from CapaDeDatos.CDD_Partidos import *
from CapaDeDatos.CDD_Clientes import *
import requests

class CapaDeNegocio():

    def listarPartidos(self):
        self.cdd = CDD_Partidos()
        partidos = self.cdd.listarPartidos()
        cotizacionDolar = self.obtenerCotizacionDolar()

        for i in partidos:
            i.precioARS = i.precioUSD * cotizacionDolar

        return partidos

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
        partido = self.cdd.buscarPartido(idPartido)
        partido.precioARS = partido.precioUSD * self.obtenerCotizacionDolar()
        return partido

    def registrarCompra(self, nuevaEntrada):
        self.cdd = CDD_Entradas()
        self.cdd.registrarCompra(nuevaEntrada)


    def altaCliente(self, cliente):
        self.cdd = CDD_Clientes()
        if self.cdd.contarClientesPorDni(cliente.dni) == 0 and cliente.dni.isdigit() and cliente.dni != "" and cliente.apellido != "" and cliente.nombre != "" and cliente.mail != "":
            self.cdd.altaCliente(cliente)
            return True
        else: return False

    def listarAsientosPartido(self, idPartido):
        self.cdd = CDD_Partidos()
        asientos = self.cdd.listarAsientosPartido(idPartido)
        if len(asientos) == 0:
            return False
        else: return asientos


    def obtenerCotizacionDolar(self):
        url_dolar = "http://ws.geeklab.com.ar/dolar/get-dolar-json.php"
        json_dolar = requests.get(url_dolar).json()
        cotizacion_dolar = float(json_dolar["libre"])
        return cotizacion_dolar


    def buscarEntradasParaPartido(self, idPartido):
        self.cdd = CDD_Entradas()
        return self.cdd.buscarEntradasParaPartido(idPartido)


        
