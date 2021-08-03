from tkinter import filedialog                          #libreria para entorno gráfico
from io import open                                     #lectura del archivo
#from webbrowser                                        #Abrir navegador automáticamente

opcion = 0
ruta = ""
archivoCargado = False
archivoLFP = []

def separador():
    print("---------------------------------------------------------------------------")

def cargarArchivo():
    global ruta, archivoCargado, archivoLFP                         #Llamando variables globales
    ruta = filedialog.askopenfilename(title="Seleccionar archivo flp")
    if ruta!="":
        print("La ruta es: " + ruta)
        archivoCargado = True
        archivoLeido = open(ruta, "r")                              #extraer el contenido de archivo con saltos de línea
        archivoLFP = archivoLeido.readlines()                       #separar en lista cada salto de línea
        print(archivoLFP)
    else:
        print("No se cargo el archivo")
        archivoCargado = False

while opcion!=4:
    separador()
    print("1. Cargar archivo")
    print("2. Mostrar reporte en consola")
    print("3. Exportar reporte")
    print("4. Salir")
    print("")
    opcion = int(input("Ingrese el número de opción que desea utilizar: "))
    if opcion == 1:
        cargarArchivo()