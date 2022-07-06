import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'pelota', 10, 'jugueteria')")

miConexion.commit()

miConexion.close()