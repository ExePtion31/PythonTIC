from io import open

'''Persistencia de datos y Manejo de archivos'''

#----------------------#
#Escritura del archivo #
#----------------------#

#Se lee un archivo de texto llamado datos.txt
archivo_texto=open("datos.txt","a") #se abre el archivo con append()
archivo_texto.write("Soy una nueva linea")
archivo_texto.close()