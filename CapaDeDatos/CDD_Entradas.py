from Conexion import Conexion


class CDD_Entradas:

    def __init__(self):
        self.con=Conexion()

    def registrarCompra(self, nuevaEntrada):
        query2 = "UPDATE vip SET libre=0 where nroAsiento={0} and idPartido={1}".format(nuevaEntrada.nroAsiento, nuevaEntrada.partido.idPartido)
        query = "INSERT INTO entrada (fechaVenta, dni, idPartido, nroAsiento) values({0},{1},{2},{3})".format(nuevaEntrada.fechaVenta, repr(nuevaEntrada.cliente.dni), nuevaEntrada.partido.idPartido, nuevaEntrada.nroAsiento)
        self.con.ejecutar(query2)
        self.con.ejecutar(query)
        self.con.conn.commit()
        print(self.con.cur.lastrowid)
        nuevaEntrada.nroComprobante = self.con.cur.lastrowid
