import sqlite3

miConexion=sqlite3.connect("GestionProductos3")


miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE CATEGORIA='confeccion'")

productos=miCursor.fetchall()

print(productos)



miConexion.commit()

miConexion.close()