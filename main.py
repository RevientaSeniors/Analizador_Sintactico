from os import startfile
from tkinter.constants import END, INSERT
from tkinter.filedialog import askopenfilename
from Analizador_Lexico import Analizador_Lexico
import tkinter

contenidoGlobal = []
#Crear la ventana
ventanaMenu = tkinter.Tk()
#Crear Frame, configurar tamaño.
frame = tkinter.Frame(ventanaMenu)
#Crear el cuadro de texto editable
cuadroTextoEditar = tkinter.Text(frame)
#Crear el cuadro de texto no editable (consola)
cuadroTexto = tkinter.Text(frame) 


def crearVentanaMenu():
    global ventanaMenu
    global frame
    global cuadroTextoEditar
    global cuadroTexto
    #Título de la ventana
    ventanaMenu.title("Menú")
    #Darle tamaño a la ventana pero lo comente porque la ventana agarra el tamaño del Frame
    #ventanaMenu.geometry("550x350")
    frame.config(width="950",height="650")
    #Dejar un tamaño fijo de la ventana
    ventanaMenu.resizable(0,0)
    #Crar Label
    label1 = tkinter.Label(frame,text="ANALIZADOR")
    label1.place(x= 50 , y=25)
    #Crear los botones
    botonCargarArchivo = tkinter.Button(frame,text="Cargar Archivo", command= bLeerArchivo)
    botonCargarArchivo.place(x=220,y=25)
    botonAnalizarArchivo = tkinter.Button(frame, text="Analizar Texto", command= bAnalizarTexto)
    botonAnalizarArchivo.place(x=370, y= 25)
    botonReporteTokens = tkinter.Button(frame, text="Reporte Tokens")
    botonReporteTokens.place(x=520, y= 25)
    botonReporteErrores = tkinter.Button(frame, text="Reporte Errores")
    botonReporteErrores.place(x=670, y= 25)
    botonReporteArbol = tkinter.Button(frame, text="Reporte Arbol")
    botonReporteArbol.place(x=820, y= 25)
    #Propiedades cuadroTextoEditar
    cuadroTextoEditar.place(x=50,y=80, width= 850, height=300)
    cuadroTextoEditar.configure(borderwidth=3, relief="solid")
    #propiedades cuadroTexto
    cuadroTexto.place(x=50,y=420,width=850,height=200)
    cuadroTexto.configure(state="disabled",borderwidth=3, relief="solid")

     #Agregar el frame a la ventana
    frame.pack()
    #Mostar la ventana
    ventanaMenu.mainloop()

def bLeerArchivo():
    global contenidoGlobal
    global cuadroTexto
    fileName = askopenfilename()
    archivo = open(fileName, 'r')
    contenido = archivo.read()
    archivo.close()
    contenidoGlobal = contenido
    cuadroTextoEditar.insert(INSERT,contenidoGlobal)

def bAnalizarTexto():
    contenidoCaja = cuadroTextoEditar.get(1.0,END)
    analizadorL = Analizador_Lexico()
    analizadorL.analizarTexto(contenidoCaja)

if __name__ == '__main__':
     crearVentanaMenu()
