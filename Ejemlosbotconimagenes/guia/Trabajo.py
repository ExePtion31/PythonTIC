import tkinter
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import webbrowser


#Raiz Principal
raiz=tkinter.Tk()
raiz.title("Trabajo en grupo 11°3")
raiz.config(bg="lemon chiffon")
raiz.geometry("960x500")


raiz1=Image.open('imagen1.png')
raiz1=raiz1.resize((500,500), Image.ANTIALIAS)
raiz1=ImageTk.PhotoImage(raiz1)

raiz2=Image.open('imagen2.png')
raiz2=raiz2.resize((500,500), Image.ANTIALIAS)
raiz2=ImageTk.PhotoImage(raiz2)

raiz3=Image.open('imagen3.png')
raiz3=raiz3.resize((500,500), Image.ANTIALIAS)
raiz3=ImageTk.PhotoImage(raiz3)

raiz4=Image.open('imagen4.png')
raiz4=raiz4.resize((500,500), Image.ANTIALIAS)
raiz4=ImageTk.PhotoImage(raiz4)


'''FUNCIONES BOTONES'''

#FUNCIÓN BOTON CON LA IMAGEN 1


def boton1():
    raizdos=tkinter.Tk()
    raizdos.geometry("960x500")
    raizdos.title("SEGUNDA RAIZ")
    raizdos.resizable(1,1)
    raizdos.config(bg="pink")
    #imgback=PhotoImage(file="fondodos.png")
    #labback=Label(raizdos,image=imgback).place(x=0,y=0)


    #Label y cuadro 1
    lab1=Label(raizdos,text="Nombre: ")
    lab1.place(x=400,y=30)
    lab1.config(fg="black",bg="dodgerBlue2",font=("Tahoma",12))

    cuadro1=Entry(raizdos,textvariable="name")
    cuadro1.config(fg="black",justify="center")
    cuadro1.place(x=500,y=30)

    #Label y cuadro 2
    lab2=Label(raizdos,text="Contraseña: ")
    lab2.place(x=400,y=60)
    lab2.config(fg="black",bg="dodgerBlue2",font=("Tahoma",12))

    cuadro2=Entry(raizdos,textvariable="pasp")
    cuadro2.config(fg="black",justify="center")
    cuadro2.place(x=500,y=60)

    #Boton
##  img=Image.open('back.png')
##  img=img.resize((50,50), Image.ANTIALIAS)
##  img=ImageTk.PhotoImage(img)

    def regreso():
        raizdos.withdraw()

    bot_re=tkinter.Button(raizdos,text="MENÚ PRINCIPAL",compound="top",command=regreso)
    bot_re.place(x=50,y=50)



#FUNCIÓN BOTON CON LA IMAGEN 2

def boton2():
    img2=Image.open('cosito.png')
    img2.show()

   # Rama=PhotoImage(file="cosito.png")
    #Lluvia=Label(Hojas,image=Rama)
    #Lluvia.place(x=0,y=0)


#FUNCIÓN BOTON CON LA IMAGEN 3

def boton3():
    greenlife=tkinter.Tk()
    greenlife.geometry("960x500")
    greenlife.title("La naturaleza")
    greenlife.resizable(1,1)
    greenlife.config(bg="black")
##    imgbackground=PhotoImage(file="fondo.png")
##    img=Label(greenlife,image=imgbackground).place(x=0,y=0)
##    img=Image.open('gaton.png')
##    img=img.resize((70,70),Image.ANTIALIAS)
##    img=ImageTk.PhotoImage(img)

    def nuevapagina():
        webbrowser.open("https://www.google.com",new=2,autoraise=True)

    def regresodos():
        greenlife.withdraw()

    bot_re=tkinter.Button(greenlife,text="MENÚ PRINCIPAL",compound="top",command=regresodos)
    bot_re.place(x=450,y=50)

    retorno=tkinter.Button(greenlife,text="PAGINA WEB",compound="top",command=nuevapagina)
    retorno.place(x=50,y=50)



#FUNCIÓN BOTON CON LA IMAGEN 4
def boton4():
    raiz.withdraw()


'''Botones'''


#BOTON 1

botonuno=tkinter.Button(raiz,image=raiz1,text="",command=boton1)
botonuno.place(x=70,y=250)
botonuno.pack(side="left",anchor="n")
botonuno.config(width="250",height="250")

#BOTON 2

botondos=tkinter.Button(raiz,image=raiz2,text="",command=boton2)
botondos.place(x=100,y=100)
botondos.pack(side="left",anchor="n")
botondos.config(width="250",height="250")

#BOTON 3

botoncuatro=tkinter.Button(raiz,image=raiz4,text="",command=boton4)
botoncuatro.place(x=100,y=100)
botoncuatro.pack(side="right",anchor="n")
botoncuatro.config(width="250",height="250")

#BOTON 4

botontres=tkinter.Button(raiz,image=raiz3,text="EXIT",command=boton3)
botontres.place(x=100,y=100)
botontres.pack(side="right",anchor="n")
botontres.config(width="250",height="250")

raiz.mainloop()

