import json
import random as r
import tkinter as tk


#iniciacion de la ventana
#configuracion de ventana     vvvvvvvvvv
ventana=tk.Tk()
ventana.title('capricho de lucas')
#anchoXalto
ventana.geometry('380x300')
ventana.configure(background='dark turquoise')

#declaracion de la funcion de la ventana:
def interfaz():
    print('hola')

#configuracion de ventana     ^^^^^^^^^^
interfaz()

with open("datos.json") as contenido:
    datos = json.loads(contenido.read())


'''----------INICIO DEL PROGRAMA----------'''

juego=input('Queres jugar? ')


if(juego == 'si'):
    '''----------JUEGOOO----------'''
    print('preguntas de lucas\n')#titulo

    contador=len(datos['quest'])#cuanta la cantidad de datos en el array
    p = r.randint(0,contador-1)#selecciona un valor aleatorio dentro del rango
    print(p)#imprime p
    print(datos["quest"][p],'\n')#imprime la pregunta
    resp = input('Verdadero o Falso (V o F): ')#pide ingreso de datos
    while(True):
        if(resp.upper() == 'V'):
            respBool = True
            break
        elif(resp.upper() == 'F'):
            respBool = False
            break
        else:
            print('hubo un error...\nReingrese la respuesta')
            continue

    if(respBool == datos['answ'][p]):
        print('Su respuesta es correcta!\n')
    else:
        print('Su respuesta es incorrecta!\n')

    print('Nos vemos en media hora....\n')



else:
    crear = input('queres agregar una nueva pregunta? ')
    '''----------CREACION DE PREGUNTASSSS----------'''
    if(crear == 'si'):
        '''----PREGUNTAS----'''
        preg = datos['quest']
        preg.append(input('Ingresa la nueva afirmacion: '))
        print(preg)
        
        '''----RESPUESTAS----'''
        resp = datos['answ']
        valor=input('Si o No?: ')
        if(valor.upper()=='SI'):
            resp.append(True)
        elif(valor.upper()=='NO'):
            resp.append(False)
        print(resp)

        '''----ACTUALIZACION DE DATOS----'''
        datos.update(quest = preg, answ = resp)
        print(datos)

        with open("datos.json",'w') as contenido:
            json.dump(datos, contenido)
    else:
        '''----------ERROR----------'''
        print('La app se va a cerrar...')

#cierre de la ventana...
ventana.mainloop()