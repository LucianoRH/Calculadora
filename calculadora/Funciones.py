# Importamos Las librerias y definimos las variables globales:
import Librerias as Lib
from tkinter import*
import math as MT

A=0

def Config_Init():
    datos_encontrados = {}
    try: 
        with open("Config.txt",'r') as Archivo:
            # Leer todas las líneas del archivo
            lineas = Archivo.readlines()
            
            # Iterar sobre cada línea
            for linea in lineas:
                # Dividir la línea en dos partes usando el signo "=" como separador
                partes = linea.split("=")
                # La primera parte será la clave y la segunda parte será el valor
                clave = partes[0].strip()
                valor = partes[1].strip()
                # Almacenar la clave y el valor en el diccionario datos_encontrados
                datos_encontrados[clave] = valor
    except FileNotFoundError:
        with open("Config.txt","w+") as Archivo:
            Archivo.writelines(Lib.Base_Config)
    return datos_encontrados

#Funcion del boton theme, cuando la entrada es  azul retorna la funcion azul y si la entrada en verde retorna la funcion verde 
#def cambioColor(t):
    if t=="azul":
        return azul
    elif t=="verde":
        return verde
    elif t=='Casio':
        return Casio
#Funcion de los botones al hacer click 
def botones(n):
    global A
    caja.insert(A, n)
    A=17
def botonesExp(n, ):
    global A
    caja.insert(A, n)
    A+=2
def FuncionE(n):
    global A
    caja.insert(A, n)
    A+=17
def  botonesLog(n):
    global A
    caja.insert(A, n)
    A+=4
def botonesInverso(n):
    global A
    caja.insert(A, n)
    A=0    
def AC(caja):
    caja.delete(0, END)
def borrar(caja):
    global A
    caja.delete(A-1,A)
    A-=1
def flechaIz():
    global A
    A-=1
def flechaDer():
    global A
    A+=1

def Seno():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,MT.sin(float(operacion)))
    A=0
    
def Cos():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,MT.cos(float(operacion)))
    A=0    

def Tan():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,MT.tan(float(operacion)))
    A=0

def verificar_signos(operacion):
        for caracter in operacion:
            if caracter == "^":
                return True
        return False    

def igual():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    operacion= 'caja.insert'+'(0,'+texto+')'
    
    caja.delete(0, END)
    caja.insert (0,exec(operacion))
    A=0

def Open_Calc(Theme, Ans, Alto, Ancho):
    # Calculadora:

    ventana= Tk()
    ventana.title("Calculadora")
    ventana.config(bg='grey63')
    #caja de texto
    global caja
    caja=Entry(ventana, font=('System 20'),bg='dark olive green')
    caja.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

    botonE=Button(ventana, text="e^x",width=Ancho, height=Alto,bg='LightSteelBlue4', command=lambda:FuncionE("e"))
    Theme= Button(ventana, text="Theme",width=Ancho, height=Alto,bg='LightSteelBlue4')
    botonCero=Button(ventana, text= "0", width=Ancho, height=Alto,bg='gray25',command=lambda:botones(0))
    botonPunto=Button(ventana, text=".", width=Ancho, height=Alto,bg='gray25',command=lambda:botones(','))
    botonPi=Button(ventana, text= "1/x", width=Ancho, height=Alto,bg='gray25',command=lambda:botonesInverso('**-1'))
    botonPorcen=Button(ventana, text="%", width=Ancho, height=Alto,bg='gray25',command=lambda:botones('%'))
    botonIgual=Button(ventana, text="=", width=Ancho, height=Alto,bg='gray25',command=igual)
    boton1=Button(ventana, text="1", width=Ancho, height=Alto,bg='gray25',command=lambda:botones(1))
    boton2=Button(ventana, text="2", width=Ancho, height=Alto,bg='gray25',command=lambda:botones(2))
    boton3=Button(ventana, text="3", width=Ancho, height=Alto,bg='gray25',command=lambda:botones(3))
    botonMas=Button(ventana, text="+", width=Ancho, height=Alto,bg='gray25',command=lambda:botones('+'))
    botonMenos=Button(ventana, text="- ", width=Ancho, height=Alto,bg='gray25',command=lambda:botones('-'))
    boton4=Button(ventana, text="4", width=Ancho, height=Alto,bg='gray25',command=lambda:botones(4))
    boton5=Button(ventana, text="5", width=Ancho, height=Alto,bg='gray25',command=lambda:botones(5))
    boton6=Button(ventana, text='6', width=Ancho, height=Alto,bg='gray25',command=lambda:botones(6))
    botonMulti=Button(ventana, text="×", width=Ancho, height=Alto,bg='gray25',command=lambda:botones('*'))
    botonDivision=Button(ventana, text='÷',width=Ancho, height=Alto,bg='gray25',command=lambda:botones('/'))
    boton7=Button(ventana, text='7', width=Ancho, height=Alto,bg='gray25',command=lambda:botones(7))
    boton8=Button(ventana, text='8', width=Ancho, height=Alto,bg='gray25',command=lambda:botones(8))
    boton9=Button(ventana, text='9', width=Ancho, height=Alto,bg='gray25',command=lambda:botones(9))

    botonDel=Button(ventana, text='Del', width=Ancho, height=Alto,bg='DeepPink4', command=borrar)
    botonAC=Button(ventana, text='AC', width=Ancho, height=Alto,bg='DeepPink4', command=AC)
    botonIzquier=Button(ventana,text='🢀', width=Ancho, height=Alto,bg='dark slate gray', command=lambda: flechaIz())
    botonDerecha=Button(ventana, text='🢂', width=Ancho, height=Alto,bg='dark slate gray', command=lambda: flechaDer())

    botonRaiz=Button(ventana, text='√ ', width=Ancho, height=Alto,bg='dark slate gray',command=lambda:botones('r'))
    botonExponente=Button(ventana,text='Exp', width=Ancho, height=Alto,bg='dark slate gray',command=lambda:botonesExp('**'))
    botonLog=Button(ventana, text='Log', width=Ancho, height=Alto,bg='dark slate gray',command=lambda:botonesLog('log'))
    botonParentesis=Button(ventana, text='( ', width=Ancho, height=Alto,bg='LightSteelBlue4',command=lambda:botones('('))
    botonParentesisII=Button(ventana, text=') ', width=Ancho, height=Alto,bg='LightSteelBlue4',command=lambda:botones(')'))
    botonseno=Button(ventana, text='sin ', width=Ancho, height=Alto,bg='dark slate gray',command=Seno)
    botoncoseno=Button(ventana, text='cos ', width=Ancho, height=Alto, bg='dark slate gray', command=Cos)
    botontangente=Button(ventana, text='tan ', width=Ancho, height=Alto, bg='dark slate gray', command=Tan)

    botonE.grid(row=1, column=4, padx=5, pady=5)
    Theme.grid(row= 1,column=0, padx=5, pady=5)
    botonParentesis.grid(row=1, column=1, padx=5, pady=5)
    botonParentesisII.grid(row=1, column=3, padx=5, pady=5)
    botonRaiz.grid(row=2, column=0, padx=5, pady=5)
    botonIzquier.grid(row=2, column=1, padx=5, pady=5)
    botonExponente.grid(row=2, column=2, padx=5, pady=5)
    botonDerecha.grid(row=2, column=3, padx=5, pady=5)
    botonLog.grid(row=2, column=4, padx=5, pady=5)
    boton7.grid(row=3, column=0, padx=5, pady=5)
    boton8.grid(row=3, column=1, padx=5, pady=5)
    boton9.grid(row=3, column=2, padx=5, pady=5)
    botonDel.grid(row=3, column=3, padx=5, pady=5)
    botonAC.grid(row=3, column=4, padx=5, pady=5)
    boton4.grid(row=4, column=0, padx=5, pady=5)
    boton5.grid(row=4, column=1, padx=5, pady=5)
    boton6.grid(row=4, column=2, padx=5, pady=5)
    botonMulti.grid(row=4, column=3, padx=5, pady=5)
    botonDivision.grid(row=4, column=4, padx=5, pady=5)
    boton1.grid(row=5, column=0, padx=5, pady=5)
    boton2.grid(row=5, column=1, padx=5, pady=5)
    boton3.grid(row=5, column=2, padx=5, pady=5)
    botonMas.grid(row=5, column=3, padx=5, pady=5)
    botonMenos.grid(row=5, column=4, padx=5, pady=5)
    botonCero.grid(row=6, column=0, padx=5, pady=5)
    botonPunto.grid(row=6, column=1, padx=5, pady=5)
    botonPi.grid(row=6, column=2, padx=5, pady=5)
    botonPorcen.grid(row=6, column=3, padx=5, pady=5)
    botonIgual.grid(row=7, column=0, padx=5, pady=5)
    botonseno.grid(row=7, column=3, padx=5, pady=5)
    botoncoseno.grid(row=6, column=4, padx=5, pady=5)
    botontangente.grid(row=7, column=4, padx=5, pady=5)




    ventana.mainloop()


