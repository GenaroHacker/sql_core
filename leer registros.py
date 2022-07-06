import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

variosproductos=miCursor.fetchall()

for producto in variosproductos:
    print(producto)
    print(producto[0])
    print("Nombre: ", producto[0], "Precio: ", producto[1], "Sección: ", producto[2])




miConexion.commit()




miConexion.close()