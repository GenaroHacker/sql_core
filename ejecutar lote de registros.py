import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 10, 'DEPORTE')")

variosProductos=[

    ("Camiseta", 10, "Deporte"),
    ("Jarrón", 20, "Cerámica"),
    ("Pelota", 5, "Deporte")


]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miConexion.commit()




miConexion.close()