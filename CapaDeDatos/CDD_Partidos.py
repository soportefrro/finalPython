from Conexion import Conexion
from Partido import Partido


class CDD_Partidos:
    def __init__(self):
        self.con=Conexion()

    def listarPartidos(self):
        query="SELECT * FROM partido p inner join estadio e on p.nombreEstadio = e.nombre;"
        self.con.ejecutar(query)
        listaPartidos=self.con.cur.fetchall()
        partidos = []
        for i in listaPartidos:
            p = Partido(i[0], i[1], i[2], i[3], i[4], i[5], None, i[6])
            partidos.append(p)
        return partidos

    def listarAsientosDisponibles(self, idPartido):
        query= "select nroAsiento, libre from vip where idPartido = {0} and libre = 1".format(idPartido)
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
            partido = Partido(par[0],par[1],par[2],par[3],par[4],par[5], None, par[6])
            return partido

    def listarAsientosPartido(self, idPartido):
        query= "select nroAsiento, libre from vip where idPartido = {0}".format(idPartido)
        self.con.ejecutar(query)
        asientos=self.con.cur.fetchall()
        return asientos
