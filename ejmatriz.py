'''Ejemplo matriz generica'''

A=[]
filas=int(input("cantidad filas: "))
columnas=int(input("cantidad columnas: "))

#Se recorre i la cantidad de veces que hay de filas
for i in range(filas):
        A.append([i]*columnas) #Repite valor agregado *cantidad columnas

A[0][0]=1
A[1][2]=5
print(A)