import sqlite3

miConexion=sqlite3.connect("GestionProductos3")


miCursor=miConexion.cursor()

miCursor.execute("UPDATE PRODUCTOS SET NOMBRE_ARTICULO='Pelota' WHERE ID=1")


miConexion.commit()

miConexion.close()