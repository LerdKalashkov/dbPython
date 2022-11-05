import psycopg2 as bd

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'posrtgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None 

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                            user=cls._USERNAME,

                                            )
            
            except Exception as e:
            
