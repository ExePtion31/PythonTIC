import tkinter      #Se importa la librería tkinter
from tkinter import PhotoImage  #Se importa la clase PhotoImage
from PIL import Image, ImageTk #Se importan las clases desde PILLOW

pera= tkinter.Tk()  #Se crea la raíz
pera.title("PERA")  #Se coloca un titulo a la raíz
pera.geometry("960x500") #Se establece un tamaño para la raíz
img=Image.open('perita.png')    #Se abre la imagen
img=img.resize((400,400), Image.ANTIALIAS) #Se coloca que la imagen del botón se pueda expandir con buena calidad
img=ImageTk.PhotoImage(img) #Se inicializa la imagen con los parámetros que esta trae

#BOTON CON IMAGEN
def fresa():            #Se define la función fresa
        img=Image.open('perita.png')    #Se abre la imagen
        img.show()  #Se ejecuta la imagen

#SE CREA EL BOTON
cereza=tkinter.Button(pera, image=img, text="",compound="top", command=fresa)
cereza.place(x=400, y=100)
cereza.pack()

pera.mainloop()
