from jinja2 import Environment, FileSystemLoader
from time import gmtime, strftime

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

    def generarHTMLInforme(self, entradasVendidas, sumatoria):

        env = Environment(loader=FileSystemLoader("CapaDePresentacion"))
        template = env.get_template("templateInforme.html")

        ENTRADAS_VENDIDAS = {}

        for i in entradasVendidas:
            datos_entrada = {
                0: str(i.nroAsiento),
                1: str(i.fechaVenta),
                2: i.cliente.nombre + ' ' + i.cliente.apellido,
                3: str(i.precioARS)
            }

            ENTRADAS_VENDIDAS[i] = datos_entrada

        idPartido = str(entradasVendidas[0].partido.idPartido)


        e = {
            'entradas': ENTRADAS_VENDIDAS,
            'sumatoria': sumatoria,
            'idPartido': idPartido
        }

        html = template.render(e)


        f = open('Informes/informe_partido'+idPartido+'_'+strftime("%Y-%m-%d-%H-%M-%S", gmtime())+'.html', 'w')
        f.write(html)
        f.close()

