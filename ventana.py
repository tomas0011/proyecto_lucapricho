def calculadora():
    import tkinter as tk

    #------------declarar funciones------------
    #suma
    def suma():
        suma=int(entrada1.get())+int(entrada2.get())
        return var.set(suma)

    #resta
    def resta():
        resta=int(entrada1.get())-int(entrada2.get())
        return var.set(resta)
    
    #multiplicacion
    def mult():
        mult=int(entrada1.get())*int(entrada2.get())
        return var.set(mult)

    #multiplicacion
    def div():
        div=int(entrada1.get())/int(entrada2.get())
        return var.set(div)
    
    #cerrar
    def cerrar():
        ventana.destroy()

    #-------------dejar de declarar funciones-----------

    #----------Creacion de la ventana------------
    ventana=tk.Tk()
    ventana.title('Calculadora Personal')
    ventana.geometry('380x380')
    ventana.configure(background='black')

    #----variables----
    var=tk.StringVar()


    #----------empieza el programa---------

    #1er numero
    e1=tk.Label(ventana,text='1er Numero: ',bg='white',fg='black')
    e1.pack(
        padx=5,
        pady=4,
        ipadx=5,
        ipady=5,
        fill=tk.X
        )
    entrada1=tk.Entry(ventana)
    entrada1.pack(
        fill=tk.X, 
        padx=5,
        pady=5, 
        ipadx=5, 
        ipady=5
        )

    #2do numero
    e2=tk.Label(ventana,text='2do Numero: ',bg='white',fg='black')
    e2.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
    entrada2=tk.Entry(ventana)
    entrada2.pack(fill=tk.X, padx=5,pady=5, ipadx=5, ipady=5)

    #-----------botones de sumadora-----------
    #boton suma
    botonSuma=tk.Button(ventana,text='suma',fg='black',command=suma)
    botonSuma.pack(side=tk.TOP)
    
    #boton resta
    botonResta=tk.Button(ventana,text='resta',fg='black',command=resta)
    botonResta.pack(side=tk.TOP)
    
    #boton multiplicador
    botonMult=tk.Button(ventana,text='multiplicar',fg='black',command=mult)
    botonMult.pack(side=tk.TOP)

    #boton division
    botondiv=tk.Button(ventana,text='dividir',fg='black',command=div)
    botondiv.pack(side=tk.TOP)
    
    #boton cierre
    botonCierre=tk.Button(ventana,text='cerrar',fg='black',command=cerrar)
    botonCierre.pack(side=tk.TOP)


    #respuesta
    res=tk.Label(ventana, bg='white', textvariable=var, padx=5, pady=5, width=20)
    res.pack()


    ventana.mainloop()

calculadora()