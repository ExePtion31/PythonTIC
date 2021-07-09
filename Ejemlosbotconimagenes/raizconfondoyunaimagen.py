import tkinter
from tkinter import *

#RAIZ LLAMADA WINDOW
WINDOW=Tk() #Se crea la raiz llamada WINDOW
WINDOW.title("PRINCIPAL WINDOW") #se le coloca el titulo a la raiz
WINDOW.resizable(1,1) #Se activa que se pueda redimencionar
WINDOW.config(bg="pink") #Se coloca un fondo rosado


#SE CREA LA IMAGEN PARA EL FONDO
imgbackground=PhotoImage(file="fondodos.png") #se carga el archivo de la imagen de fondo a una variable
labelfondo=Label(WINDOW, image=imgbackground).place(x=0, y=0) #Se asigna la variable con la imagen a un label

#SE GUARDA UNA IMAGEN PARA MOSTRAR
img=PhotoImage(file="perita.png") #se carga el archivo de la imagen a una variable
labelimagenuno=Label(WINDOW, image=img).place(x=500, y=130) #Se asigna la variable con la imagen a un label

WINDOW.mainloop()