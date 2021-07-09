#------main function--------
def main():
    processData();
#---------------------------

#-----capturar datos--------
def processData():
    salarioBase, horasExt, bonificacion = input().split()
    salarioBase = float(salarioBase)
    horasExt = int(horasExt)  
    bonificacion = int(bonificacion)
    totalHoraExt = 0
    totalBonificacion = 0

    if horasExt > 0:
        totalHoraExt = valorHoras(salarioBase) * horasExt
    if bonificacion > 0:
        totalBonificacion = bonificaciones(salarioBase)

    salarioTotal = salarioBase + totalHoraExt + totalBonificacion
    salarioDesc = descuentos (salarioTotal)
    print(round(salarioTotal, 1), round(salarioDesc, 1))    
#---------------------------

#-------valor por hora-------
def valorHoras(salarioBase):    
    valorHora = (salarioBase / 185) + (((salarioBase / 185) * 45) / 100)

    return valorHora
#----------------------------

#-------valor bonificaciones-----
def bonificaciones(salarioBase):
    bonificacion = (salarioBase * 3.5) / 100
    
    return bonificacion
#--------------------------------

#---------descuentos salario-----
def descuentos (salarioTotal):
    descuento = salarioTotal - ((salarioTotal * 10.5) / 100)

    return descuento
#--------------------------------


#------------main-------------
if __name__ == "__main__":
        main();
#-----------------------------        
