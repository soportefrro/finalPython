from CapaDeDatos.CDD_Partidos import *

class CapaDeNegocio():

    def listarPartidos(self):
        self.cdd = CDD_Partidos()
        return self.cdd.listarPartidos()

    def listarAsientos(self):
        sarasa = "pija"

