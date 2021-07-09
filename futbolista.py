#-----main function-----
def main():
    captureData()
#----------------------    

#-----capture data-----
def captureData():
    nregistros = input()
    nregistros = int(nregistros)
    i = 1
    contador = 0;

    while i <= nregistros: 
        titulos, companeros, goles, titulosI, oferta = input().split();
        titulos = int(titulos)
        companeros = int(companeros)
        goles = int(goles)
        titulosI = int(titulosI)
        oferta = int(oferta)

        if titulos > 4 and companeros > 3 and goles <= 30 and titulosI >= 3:
            print(oferta) 
        else:
            contador += 1

        if contador == nregistros:
            print("NO DISPONIBLE")

        i+=1    
#----------------------   


#------main-----------
if __name__ == "__main__":
    main()
#--------------------