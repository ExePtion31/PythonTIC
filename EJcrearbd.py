import sqlite3
miConexion=sqlite3.connect("primerBase")
miCursor=miConexion.cursor()
miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER)")