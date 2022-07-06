import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

variosproductos=miCursor.fetchall()

print(variosproductos)

miConexion.commit()




miConexion.close()