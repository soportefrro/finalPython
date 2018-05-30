from Conexion import Conexion
from Partido import Partido


class CDD_Partidos:
    def __init__(self):
        self.con=Conexion()

    def listarPartidos(self):
        query="Select * from partido"
        self.con.ejecutar(query)
        partidos=self.con.cur.fetchall()
        return partidos

    def listarAsientos(self, idPartido):
        query= "select * from vip where idPartido = {0}".format(idPartido)
        self.con.ejecutar(query)
        asientos=self.con.cur.fetchall()
        return asientos

    def buscarPartido(self, idPartido):
        query = "SELECT * FROM partido where idPartido = {0}".format(idPartido)
        self.con.ejecutar(query)
        par = self.con.cur.fetchone()
        if par == None:
            return None
        else:
            partido = Partido(par[0],par[1],par[2],par[3],par[4],par[5],par[6])
            return partido
