'''Ejemplo manejo base de datos'''
#-----------------------------------------------------------------------
#Ejemplo con instrucciones para utilizar correctamente una base de datos
#-----------------------------------------------------------------------

import sqlite3  #Se llama la libreria sqlite3

conn=sqlite3.connect("primerbasededatos.db") #conecta la base de datos 
cur=conn.cursor()
cur.execute("SELECT * from basedatospaises") #Ejecuta la base de datos
print(cur.fetchone()) #imprimir una fila
print(cur.fetchall()) #Imprimir varias filas

#Imprimir fila por fila en orden
for fila in cur.execute("SELECT * from basedatospaises"):
        print(fila)

#Uso de Where para consultar los valores de una fila
codigo=("AFG",)
cur.execute("SELECT * from basedatospaises WHERE CODIGO = ?", codigo)
print(cur.fetchone())

#Crear una lista con una fila de la base de datos
codigo=("NLD",)
cur.execute("SELECT * from basedatospaises WHERE CODIGO = ?", codigo)
filaDos=cur.fetchone()
print(filaDos)
print(type(filaDos))

#Convertir en lista y agregar un nuevo elemento a la lista
filaDos=list(filaDos)
filaDos.append("soy un nuevo elemento en la lista") 
print(filaDos)

