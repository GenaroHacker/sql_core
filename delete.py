import sqlite3

miConexion=sqlite3.connect("GestionProductos3")

miCursor=miConexion.cursor()


miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=2")




miConexion.commit()

miConexion.close()