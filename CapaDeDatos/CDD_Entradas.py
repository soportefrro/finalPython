from Conexion import Conexion


class CDD_Entradas:

    def __init__(self):
        self.con=Conexion()

    def registrarCompra(self, nuevaEntrada):
        print(nuevaEntrada.fechaVenta, nuevaEntrada.nroComprobante, repr(nuevaEntrada.cliente.dni), nuevaEntrada.partido.idPartido, nuevaEntrada.nroAsiento)
        query = "INSERT INTO entrada values({0},{1},{2},{3},{4})".format(nuevaEntrada.fechaVenta, nuevaEntrada.nroComprobante, repr(nuevaEntrada.cliente.dni), nuevaEntrada.partido.idPartido, nuevaEntrada.nroAsiento)
        self.con.ejecutar(query)
        self.con.conn.commit()
