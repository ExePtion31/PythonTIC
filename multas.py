#-----main function-------
def main():
    capturarData();
#-------------------------

#----capture data---------
def capturarData():
    distancia, vMax, tiempo = input().split()
    distancia = int(distancia)
    vMax = int(vMax)
    tiempo = int(tiempo)
    tiempoH = float(convertionT(tiempo))  
    distanciaKM = float(convertionD(distancia))
    Vusuario = distanciaKM / tiempoH

    prints(distancia, vMax, tiempo, Vusuario)
#-------------------------

#-----convertionT---------
def convertionT(tiempo):
    tiempoH = tiempo / 3600
    return tiempoH
#-------------------------

#-----convertionD---------
def convertionD(distancia):
    distanciaKM = distancia / 1000
    return distanciaKM
#-------------------------

#-------print-------------
def prints(distancia, vMax, tiempo, Vusuario):
    if(distancia < 0 or vMax < 0 or tiempo <0):
        print("ERROR")
    elif(Vusuario < vMax):
        print("NORMAL")
    elif(Vusuario < (vMax + (vMax * 0.25))):
        print("MULTA")
    elif(Vusuario > (vMax + (vMax * 0.25))):
        print("CURSO")   
#------------------------    

#----------main----------
if __name__ == "__main__":
        main()
#------------------------        