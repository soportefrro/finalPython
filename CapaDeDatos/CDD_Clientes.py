from Cliente import Cliente
from Conexion import Conexion

class CDD_Clientes:
    def __init__(self):
        self.con=Conexion()

    def buscarCliente(self, dni):
        query="Select * from cliente where dni={0}".format(dni)
        self.con.ejecutar(query)
        cli=self.con.cur.fetchone()
        if cli== None:
            return None
        else:
            cliente= Cliente(cli[0],cli[1],cli[2],cli[3])
            return cliente
