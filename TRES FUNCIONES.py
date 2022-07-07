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


columnas = """
        CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)"""

#CrearTabla("JAJA","PEPE",columnas)
InsertarRegistro("JAJA","INSERT INTO PEPE VALUES (NULL,'BALON',10,'DEPORTE')")
InsertarVariosRegistros("JAJA",[
    "INSERT INTO PEPE VALUES (NULL,'BALON',10,'DEPORTE')",
    "INSERT INTO PEPE VALUES (NULL,'JARRON',20,'CERAMICA')",
    "INSERT INTO PEPE VALUES (NULL,'PELOTA',5,'DEPORTE')"
])
