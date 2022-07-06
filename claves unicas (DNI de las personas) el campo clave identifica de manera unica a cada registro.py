import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()







miConexion.commit()

miConexion.close()