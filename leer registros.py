import sqlite3

miConexion=sqlite3.connect("GestionProductos2")


miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    CATEGORIA VARCHAR(20))
''')

productos=[

    ("pelota", 10, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("zapatos", 20, "accesorios"),
    ("camisa", 25, "confeccion")
    
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()