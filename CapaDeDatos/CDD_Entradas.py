from Conexion import Conexion
from Entrada import Entrada


def buscarCliente(param):
    pass


class CDD_Entradas:

    def __init__(self):
        self.con=Conexion()

    def registrarCompra(self, nuevaEntrada):
        query2 = "UPDATE vip SET libre=0 where nroAsiento={0} and idPartido={1}".format(nuevaEntrada.nroAsiento, nuevaEntrada.partido.idPartido)
        query = "INSERT INTO entrada (fechaVenta, dni, idPartido, nroAsiento, precioUSD, cotizacionDolar, precioARS) values({0},{1},{2},{3},{4},{5},{6})".format(nuevaEntrada.fechaVenta, repr(nuevaEntrada.cliente.dni), nuevaEntrada.partido.idPartido, nuevaEntrada.nroAsiento, nuevaEntrada.partido.precioUSD, nuevaEntrada.cotizacionVenta, nuevaEntrada.partido.precioARS)
        self.con.ejecutar(query2)
        self.con.ejecutar(query)
        self.con.conn.commit()
        nuevaEntrada.nroComprobante = self.con.cur.lastrowid

    def buscarEntradasParaPartido(self, idPartido):
        query = "SELECT * from entrada where idPartido = {0}".format(idPartido)
        self.con.ejecutar(query)
        listaEntradas = self.con.cur.fetchall()
        if listaEntradas== None:
            return None
        else:
            entradas = []
            for ent in listaEntradas:
                cliente = buscarCliente(ent[2])
                e = Entrada(ent[1],ent[2],ent[3],ent[0], ent[4], ent[5])
                entradas.append(e)
            return entradas


