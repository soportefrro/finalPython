import pymysql


class Conexion():
    def __init__(self):
        try:
            d=dict()
            d['user']= 'root'
            d['password']= 'root'
            d['host']='localhost'
            d['database']='mundial2018'
            self.conn = pymysql.connect(**d)
            self.cur = self.conn.cursor()
        except Exception as f:
            print("Error al ejecutar SQL " + str(f))

    def ejecutar(self, query):
        self.cur.execute(query)


if __name__ == '__main__':
    con = Conexion()

