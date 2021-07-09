import tkinter

nombre = "Paola"
def mostrar(n):
        mensaje.configure(text="Hola")

ventana=tkinter.Tk()
mensaje=tkinter.Label(ventana,text="",width=12)
mensaje.grid(row=1,column=1)
boton=tkinter.Button(ventana,text="Saludo",command=mostrar(nombre))
boton.grid()

ventana.mainloop()
