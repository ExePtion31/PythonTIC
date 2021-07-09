#------main function-----
def main():
    database()


#-----database------
def database():
    articulos = {
        1 : [123, "Desinfectante X", 8500, 250],
        2 : [456, "Jabon Y", 1900, 320],
        3: [789, "Detergente Z", 12000, 410]
    }
    captureData(articulos)

#----capture data-----
def captureData(articulos):
    nClientes = int(input("Ingrese la cantidad de clientes: "))
    ProductosCLientes = {}

    for i in range(0, nClientes):
        print("<------Cliente #",i+1,"-------->")
        nDesinfectante = int(input("Cantidad de Desinfectante X que desea llevar: "))
        nJabon = int(input("Cantidad de Jabón Y que desea llevar: "))
        nDetergente  = int(input("Cantidad de Detergente Z que desea llevar: "))
        ProductosCLientes[i] = [nDesinfectante, nJabon, nDetergente]
    totalPagar(ProductosCLientes)   
    totalVentas(ProductosCLientes)
    mayorVendido(ProductosCLientes, articulos)
    existencia(ProductosCLientes, articulos)
    mayorVendidoInfo(ProductosCLientes, articulos)


#---total pagar-----
def totalPagar(ProductosCLientes):
    productos = ProductosCLientes
    print("<---TOTAL----->")
    for i in productos:
        total = (productos[i][0] * 8500) + (productos[i][1] * 1900) + (productos[i][2] * 12000)
        print("Total del cliente #",i+1,": ",total)


#-----total ventas-----
def totalVentas(ProductosCLientes):
    productos = ProductosCLientes
    totalDesin = 0
    totalJabon = 0
    totalDeter = 0
    for i in productos:
        totalDesin += productos[i][0] * 8500 
        totalJabon += productos[i][1] * 1900 
        totalDeter += productos[i][2] * 12000
    total = (totalDesin, totalJabon, totalDeter)
    print("<----TOTAL VENTAS POR PRODUCTO----->")  
    print("Desinfectante X: ",total[0],"\nJabón Y: ",total[1],"\nDetergente Z: ",total[2])  


#-------mayor vendido--------
def mayorVendido(ProductosCLientes, articulos):
    articulosDB = articulos
    productos = ProductosCLientes
    totalDesin = 0
    totalJabon = 0
    totalDeter = 0
    for i in productos:
        totalDesin += productos[i][0] 
        totalJabon += productos[i][1] 
        totalDeter += productos[i][2] 
    total = (totalDesin, totalJabon, totalDeter)
    print("<----PRODUCTO MAS VENDIDO VENDIDO----->")
    if total[0] > total[1] and total[0] > total[2]:
        productoM = articulosDB[1][1]
    elif total[1] > total[0] and total[1] > total[2]:    
        productoM = articulosDB[2][1]
    else:
        productoM = articulosDB[3][1]
    print("Nombre: ",productoM)    

#-----Total existencias------
def existencia(ProductosCLientes, articulos):
    articulosDB = articulos
    productos = ProductosCLientes
    totalDesin = 0
    totalJabon = 0
    totalDeter = 0
    for i in productos:
        totalDesin += productos[i][0] 
        totalJabon += productos[i][1] 
        totalDeter += productos[i][2] 
    total = (totalDesin, totalJabon, totalDeter)
    existencias = ((articulosDB[1][3]-total[0]), (articulosDB[2][3]-total[1]), (articulosDB[3][3]-total[2]))
    print("<-----TOTAL EXISTENCIAS----->")
    print("Existencias Desinfectante X: ",existencias[0],"\nExistencias Jabón Y: ",existencias[1],"\nExistencias Detergente Z: ",existencias[2])



#-------Info mayor vendido--------
def mayorVendidoInfo(ProductosCLientes, articulos):
    articulosDB = articulos
    productos = ProductosCLientes
    totalDesin = 0
    totalJabon = 0
    totalDeter = 0
    for i in productos:
        totalDesin += productos[i][0] 
        totalJabon += productos[i][1] 
        totalDeter += productos[i][2] 
    total = (totalDesin, totalJabon, totalDeter)
    print("<----INFORMACIÓN PRODUCTO MAS VENDIDO VENDIDO----->")
    if total[0] > total[1] and total[0] > total[2]:
        productoM = (articulosDB[1][0], articulosDB[1][1], articulosDB[1][2], total[0])
    elif total[1] > total[0] and total[1] > total[2]:    
        productoM = (articulosDB[2][0], articulosDB[2][1], articulosDB[2][2], total[1])
    else:
        productoM = (articulosDB[3][0], articulosDB[3][1], articulosDB[3][2], total[2])
    print("ID: ",productoM[0], "\nNombre: ",productoM[1],"\nValor: ",productoM[2],"\nVendidos: ",productoM[3])    



#-----main--------
if __name__ == "__main__":
    main()