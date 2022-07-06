import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(5) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[
    ("AR01", "pelota", 10, "jugueteria"),
    ("AR02", "pantalon", 20, "confeccion"),
    ("AR03", "zapatos", 30, "accesorios"),
    ("AR04", "camiseta", 40, "deportes"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()

miConexion.close()