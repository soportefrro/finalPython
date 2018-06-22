from datetime import date

from CapaDeNegocio.CapaDeNegocio import CapaDeNegocio
from Entrada import Entrada


class Compra():

    def confirmarCompra(self, cliente, idPartido, idAsiento):
        cdn = CapaDeNegocio()
        partido = cdn.buscarPartido(idPartido)
        print(partido.idPartido, partido.pais1)
        nuevaEntrada = Entrada(cliente, partido, date.today().strftime('%Y%m%d') , idAsiento) #instancio una nueva entrada

        cdn.registrarCompra(nuevaEntrada)

