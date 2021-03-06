import tkinter

#Función display para mostrar en pantalla cuando presionen el botón
def display():
        name = textVar.get()
        ch = choice.get()
        if ch == 1:
            message = "Hello "+name
        elif ch == 2:
            message = "Goodbye "+name
        else:
            message = ""
        messageLabel.configure(text=message)

#Se crea la ventana principal llamada top
top = tkinter.Tk()

#Se crea un cuadro de texto con su respectiva variable para guardar valores
textVar = tkinter.StringVar("")
textEntry = tkinter.Entry(top,textvariable=textVar,width=12)
textEntry.grid(row=0,column=0)

#Se crea un label o mensaje en la ventana
messageLabel = tkinter.Label(top,text="",width=12)
messageLabel.grid(row=1,column=0)

#Se crean radio botones para seleccionar una opción de saludo o despedida
choice = tkinter.IntVar(0)
helloButton = tkinter.Radiobutton(top,text="Hello",variable=choice,
                value=1,command=display)
helloButton.grid(row=1,column=1)
goodbyeButton = tkinter.Radiobutton(top,text="Goodbye",variable=choice,
                    value=2,command=display)
goodbyeButton.grid(row=1,column=2)

#Se crea un botón para cerrar la ventana o raiz principal
quitButton = tkinter.Button(top,text="Quit",command=top.destroy)
quitButton.grid(row=1,column=3)

tkinter.mainloop()