from Conexion import Conexion
from Entrada import Entrada
from CapaDeDatos.CDD_Clientes import *
from CapaDeDatos.CDD_Partidos import *


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
                self.cddCliente = CDD_Clientes()
                cliente = self.cddCliente.buscarCliente(ent[2])

                self.cddPartido = CDD_Partidos()
                partido = self.cddPartido.buscarPartido(ent[3])

                e = Entrada(ent[1],cliente,partido,ent[0], ent[4], ent[6], ent[5], ent[7])
                entradas.append(e)
            return entradas


