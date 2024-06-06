# Importamos Las librerias y definimos las variables globales:

import tkinter as tk
import math as mt
import Librerias as Lib

Archivo=""


# Definimos las funciones:



# Abrimos la configuracion de la software:
try: 
    Archivo = open('Config.txt','r')
except FileNotFoundError:
    Archivo = open("Config.txt","w+")
    Archivo.writelines(Lib.Base_Config)

