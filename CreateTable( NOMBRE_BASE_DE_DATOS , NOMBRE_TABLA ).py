import sqlite3

def CreateTable( NOMBRE_BASE_DE_DATOS , NOMBRE_TABLA ):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute('''
        CREATE TABLE ''' + NOMBRE_TABLA + ''' (
        CODIGO_ARTICULO VARCHAR(5) PRIMARY KEY,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
    ''')
    miConexion.commit()
    miConexion.close()

CreateTable("BASE BUENARDA","TABLA_PRODUCTOS")