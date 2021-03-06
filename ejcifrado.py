'''Ejemplo cifrado y descifrado '''
try:
    #Variable indica la cantidad de desplazamientos en la encriptación
    desplazamiento=int(input("Ingresa el desplazamiento: "))

    #Subrutina o función para encriptar el texto
    def codificacion(texto):
            cifrado=""
            #Se compara si el texto esta en mayusculas o minusculas++
            if texto==texto.upper():
                    lista="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            else:
                    lista="abcdefghijklmnñopqrstuvwxyz"

            #Ciclo que recorre el texto con la variable caracter
            for caracter in texto:
                    if caracter in lista:
                        #Se chequea la posición para el desplazamiento
                        if ((lista.index(caracter))+desplazamiento)<25:
                        #si la posición llega hasta z se cifra así
                            cifrado+=lista[((lista.index(caracter)) 
                                        +desplazamiento)]
                                        
                        else:
                        #si la posición supera la posición z se cifra así:   
                            cifrado+=lista[((lista.index(caracter)) 
                                        +desplazamiento)-27]
                    #Si el caracter no esta en la lista lo deja original
                    else:
                        cifrado+=caracter
            return cifrado
       
    #Subrutina o función para desencriptar el texto
    def descodificacion(texto):
            
            descifrado=""
            #Se compara si el texto esta en mayusculas o minusculas
            if texto==texto.upper():
                lista="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            else:
                lista="abcdefghijklmnñopqrstuvwxyz"
            #Ciclo que recorre el texto con la variable caracter
            for caracter in texto:
                    if caracter in lista:
                        #Se chequea la posición para el desplazamiento
                        if ((lista.index(caracter))+desplazamiento)<25:
                        #si la posición llega hasta z se descifra así:    
                            descifrado+=lista[((lista.index(caracter)) 
                                        -desplazamiento)]
                        else:
                        #si posición supera la posición z se descifra así:      
                            descifrado+=lista[((lista.index(caracter)) 
                                        -desplazamiento)-27]
                    #Si el caracter no esta en la lista lo deja original
                    else:
                        descifrado+=caracter
            return descifrado
    
    frase=input("Ingresa la frase a codificar: ")
    print("soy la frase codificada: ", codificacion(frase))
    print("soy la frase descodificada: ",descodificacion(codificacion(frase)))
    
#Si ocurre un error se mostrara este mensaje al usuario
except:
     (print("Se ha producido un error vuelve a intentarlo"))