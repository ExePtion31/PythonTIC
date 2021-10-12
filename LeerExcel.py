import pandas as pd
df = pd.read_excel("DataBase.xlsx")

#----main---------
def main():
    guardarDatos(); 
#-----------------

#----cargar archivo------
def guardarDatos():
    datos = df.values;
    procesarDatos(datos)

#----procesar datos-----
def procesarDatos(datos):
    for i in range(len(datos)):
        for j in range (len(datos[i])):
            if j == 0 or j == 1:
                datos[i][j] = datos[i][j].capitalize()
            elif j == 3:
                if datos[i][j].lower() == "hombre" or datos[i][j].lower() == "m" or datos[i][j].lower() == "masculino":
                    datos[i][j] = "Masculino"
                elif datos[i][j].lower() == "f" or datos[i][j].lower() == "mujer" or datos[i][j].lower() == "femenino" or datos[i][j].lower() == "abuela" or datos[i][j].lower() == "niña":
                    datos[i][j] = "Femenino"  
    guardarData(datos)

#-----guardar data-------
def guardarData(datos):
    df = pd.DataFrame(datos, columns=['Nombre', 'Apellido', 'NIT', 'Género'])
    df.to_excel("DataFinal.xlsx")    

#---main-----
if __name__ == "__main__":
    main()

