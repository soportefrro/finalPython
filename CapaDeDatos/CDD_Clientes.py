from Cliente import Cliente
from Conexion import Conexion

class CDD_Clientes:
    def __init__(self):
        self.con=Conexion()

    def buscarCliente(self, dni):

        query="Select * from cliente where dni={0}".format(repr(dni))
        self.con.ejecutar(query)
        cli=self.con.cur.fetchone()
        if cli== None:
            return None
        else:
            cliente= Cliente(cli[0],cli[1],cli[2],cli[3])
            return cliente

    def altaCliente(self, cliente):
        query = ("INSERT INTO cliente values({0},{1},{2},{3})").format(repr(cliente.dni), repr(cliente.nombre), repr(cliente.apellido), repr(cliente.mail))
        self.con.ejecutar(query)
        self.con.conn.commit()

    def contarClientesPorDni(self, dni):
        query = "SELECT COUNT(*) FROM cliente WHERE dni={0}".format(repr(dni))
        self.con.ejecutar(query)
        cant = self.con.cur.fetchone()
        return cant[0]

