import sqlite3


def InsertarRegistro(NOMBRE_BASE_DE_DATOS, REGISTRO):
    miConexion=sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    miCursor=miConexion.cursor()
    miCursor.execute(REGISTRO)
    miConexion.commit()
    miConexion.close()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 10, 'DEPORTE')")

variosProductos=[

    ("Camiseta", 10, "Deporte"),
    ("Jarrón", 20, "Cerámica"),
    ("Pelota", 5, "Deporte")


]

"INSERT INTO PRODUCTOS VALUES (?,?,?)"

miConexion.commit()




miConexion.close() 