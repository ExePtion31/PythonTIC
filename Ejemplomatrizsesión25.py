'''Ejemplo matriz sesión 25'''

A=[]
m=int(input("cantidad filas: "))
n=int(input("cantidad columnas: "))

for i in range(m):
        A.append([0]*n)
        
for j in range(m):
    for k in range(n):
        print("Ingresa un nuevo elemento para la matriz: ")
        A[j][k]=int(input())
print(A)