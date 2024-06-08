# Importamos Las librerias y definimos las variables globales:
import Funciones as FuncionesCal

Archivo=""
Theme=0
Ans=0
alto=0
ancho=0

# Abrimos la configuracion de software:
Archivo=FuncionesCal.Config_Init()
Theme=int(Archivo['Theme'])
Ans=int(Archivo['Ans'])
Alto=int(Archivo['Alto'])
Ancho=int(Archivo['Ancho'])

FuncionesCal.Open_Calc(Theme,Ans,Alto,Ancho)
