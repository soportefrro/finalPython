from Conexion import Conexion

class CDD_Partidos:
    def __init__(self):
        self.con=Conexion()

    def listarPartidos(self):
        query="Select * from partido"
        self.con.ejecutar(query)
        partidos=self.con.cur.fetchall()
        return partidos
