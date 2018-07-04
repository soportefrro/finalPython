from jinja2 import Environment, FileSystemLoader

class GenerarHTML():
    informe = 1

    def generarHTMLEntrada(self, entrada):
        env = Environment(loader=FileSystemLoader("CapaDePresentacion"))
        template = env.get_template("templateEntrada.html")

        datosEntrada = {
            'pais1': entrada.partido.pais1,
            'pais2': entrada.partido.pais2,
            'nombreapellido': entrada.cliente.nombre + " " + entrada.cliente.apellido,
            'dni': entrada.cliente.dni,
            'estadio': entrada.partido.estadio,
            'precio': entrada.partido.precioUSD,
            'fecha': entrada.partido.fecha,
            'instancia': entrada.partido.instancia,
            'asiento': entrada.nroAsiento,
            'numeroentrada': entrada.nroComprobante
            }

        numeroEntrada = str(entrada.nroComprobante)
        html = template.render(datosEntrada)

        f = open('Entradas_Vendidas/entrada_nro_'+numeroEntrada+'.html', 'w')
        f.write(html)
        f.close()

    def generarHTMLInforme(self, entradasVendidas, sumatoria):
        env = Environment(loader=FileSystemLoader("CapaDePresentacion"))
        template = env.get_template("templateInforme.html")
        entradas = []

        for i in entradasVendidas:
            e = {
                'nroAsiento': i.nroAsiento,
                'fechaVenta': i.fechaVenta,
                'nombreapellido': i.cliente.nombre + " " + i.cliente.apellido,
                'importe': i.partido.precioUSD * i.cotizacionVenta,
                'sumatoria': sumatoria
                }
            entradas.append(e)

            html = template.render(entradas)

        f = open('Entradas_Vendidas/informe_nro_'+self.informe+'.html', 'w')
        f.write(html)
        self.informe = self.informe + 1
        f.close()

