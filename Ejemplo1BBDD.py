import sqlite3

# Abrir-Crear conexión
miConexion=sqlite3.connect("PrimeraBase")

# Creamos puntero
miCursor=miConexion.cursor()

# Ejecutar query (consulta) SQL
# Manejar los resultados de la query (consulta).
# Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete)
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 10, 'DEPORTE')")

miConexion.commit()

# Cerrar puntero
# Cerrar conexión
miConexion.close()