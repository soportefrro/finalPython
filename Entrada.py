class Entrada():
    ultimoNumComprobante = 1

    def __init__(self, cliente, partido, fechaVenta, nroComprobante, nroAsiento):
        self.cliente = cliente
        self.partido = partido
        self.fechaVenta = fechaVenta
        self.nroComprobante = nroComprobante
        self.nroAsiento = nroAsiento
        self.actualizarUltimoNumComprobante()

    def actualizarUltimoNumComprobante(self):
        self.ultimoNumComprobante += 1






