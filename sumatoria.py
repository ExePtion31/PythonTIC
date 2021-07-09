n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
sumatoria = 0;

if(n>m):
    while n > m:
        print("El numero n tiene que ser menor o igual a m")
        n = int(input("Ingrese el valor de n: "))
        m = int(input("Ingrese el valor de m: "))
 
while n <= m:
    sumatoria += n;
    n+=1;

print("El resultado de la sumatoria es: ",sumatoria) 