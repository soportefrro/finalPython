from jinja2 import Environment, FileSystemLoader

class GenerarHTML():

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



