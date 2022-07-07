import sqlite3

def CrearTabla( NOMBRE_BASE_DE_DATOS , NOMBRE_TABLA , ESTRUCTURA_TABLA ):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute('''
        CREATE TABLE ''' + NOMBRE_TABLA + ''' ( ''' + ESTRUCTURA_TABLA + ''' )
    ''')
    miConexion.commit()
    miConexion.close()

def InsertarRegistro(NOMBRE_BASE_DE_DATOS, REGISTRO):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute(REGISTRO)
    miConexion.commit()
    miConexion.close()

def InsertarVariosRegistros(NOMBRE_BASE_DE_DATOS, VARIOS_REGISTROS):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    for i in VARIOS_REGISTROS:
        miCursor.execute(i)
    miConexion.commit()
    miConexion.close()

def LeerRegistros(NOMBRE_BASE_DE_DATOS, NOMBRE_TABLA):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM " + NOMBRE_TABLA)
    registros=miCursor.fetchall()
    miConexion.close()
    return registros

def ActualizarRegistro(NOMBRE_BASE_DE_DATOS, REGISTRO):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute(REGISTRO)
    miConexion.commit()
    miConexion.close()

def EliminarRegistro(NOMBRE_BASE_DE_DATOS, REGISTRO):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute(REGISTRO)
    miConexion.commit()
    miConexion.close()

def EjecutarComando(NOMBRE_BASE_DE_DATOS, COMANDO):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute(COMANDO)
    miConexion.commit()
    miConexion.close()

columnas = """
        CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)"""

CrearTabla("BaseProductos","TablaProductos",columnas)
InsertarRegistro("BaseProductos","INSERT INTO TablaProductos VALUES (NULL,'BALON',10,'DEPORTE')")
InsertarVariosRegistros("BaseProductos",[
    "INSERT INTO TablaProductos VALUES (NULL,'BALON',10,'DEPORTE')",
    "INSERT INTO TablaProductos VALUES (NULL,'JARRON',20,'CERAMICA')",
    "INSERT INTO TablaProductos VALUES (NULL,'PELOTA',5,'DEPORTE')"
])
print(LeerRegistros("BaseProductos","TablaProductos"))
ActualizarRegistro("BaseProductos","UPDATE TablaProductos SET NOMBRE_ARTICULO='PELO8TA' WHERE CODIGO_ARTICULO=3")
EliminarRegistro("BaseProductos","DELETE FROM TablaProductos WHERE CODIGO_ARTICULO=3")