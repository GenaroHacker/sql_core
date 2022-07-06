import sqlite3

# Abrir-Crear conexión
miConexion=sqlite3.connect("PrimeraBase")

# Crear puntero
miCursor=miConexion.cursor()

# Ejecutar query (consulta) SQL
# Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete)

# (Tabla ya creada)
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
# (Elemento ya insertado)
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 10, 'DEPORTE')")

# Confirmar cambios
miConexion.commit()

# Cerrar conexión
miConexion.close()