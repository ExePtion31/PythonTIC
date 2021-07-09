#---main function----
def main():
    createDB()

#----DB-------
def createDB():
    productos = {1:["Manzanas", 6000, 25], 
                2:["Limones", 2900, 555], 
                3:["Peras", 2700, 33],
                4:["Arandanos", 9300, 34],
                5:["Tomates", 2100, 42],
                6:["Fesas", 4100, 10],
                7:["Helado", 4500, 41],
                8:["Galletas", 500, 8],
                9:["Chocolates", 4600, 999],
                10:["Jamon", 15000, 10]}    
    funcionesTienda(productos)        

#------funciones tienda-----
def funcionesTienda(productos):
    operacion = input()
    if operacion.upper() == "AGREGAR":
        addFunction(productos)
    elif operacion.upper() == "ACTUALIZAR":
        updateFunction(productos)
    elif operacion.upper() == "BORRAR":   
        deleteFunction(productos) 

#-----solicitar datos------
def getDataUser():
    idPrroducto, nombreProducto, precioProducto, invProducto = input().split()
    idPrroducto = int(idPrroducto)
    precioProducto = int(precioProducto)
    invProducto = int(invProducto)

    data = {"id":idPrroducto, "name":nombreProducto, "precio":precioProducto, "inv":invProducto}
    return data

#----add function-----
def addFunction(productos):
    data = getDataUser()

    if data["id"] in productos:
        print("ERROR")
    else:
        productos[data["id"]] = [data["name"], data["precio"], data["inv"]]
        calcularData(productos)
            
#----update function--------
def updateFunction(productos):
    data = getDataUser()

    if data["id"] in productos:
        productos[data["id"]] = [data["name"], data["precio"], data["inv"]]
        calcularData(productos)
    else:
        print("ERROR")    

#-----delete function--------
def deleteFunction(productos):
    data = getDataUser()

    if data["id"] in productos:
        del productos[data["id"]]
        calcularData(productos)
    else:
        print("ERROR")    


#---------cancular data------
def calcularData(productos):
    preciomax = 0
    productomax = ""
    productomin = ""
    preciomin = productos[1][1]
    promedio = 0
    contador = 0
    valorinv = 0
    
    for i in productos:
        precio = productos[i][1]
        if preciomax < precio:
            preciomax = precio
            productomax = productos[i][0]
        if precio < preciomin:
            preciomin = precio
            productomin = productos[i][0]
        promedio += precio    
        contador += 1
        valorinv += (productos[i][1] * productos[i][2])

    promedio /= contador   
    print(productomax, productomin, round(promedio,1), "{:.1f}".format(valorinv))

#-------main------
if __name__ == "__main__":
    main()