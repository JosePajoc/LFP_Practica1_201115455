from tkinter import filedialog                          #libreria para entorno gráfico
from io import open                                     #lectura del archivo
#from webbrowser                                        #Abrir navegador automáticamente

opcion = 0
ruta = ""
archivoCargado = False
archivoLFP = []
curso = ""
parametros = ""
alumnos = []

def separador():
    print("---------------------------------------------------------------------------")

def cargarArchivo():
    global ruta, archivoCargado, archivoLFP              #Llamando variables globales
    ruta = filedialog.askopenfilename(title="Seleccionar archivo flp")
    if ruta!="":
        print("La ruta es: " + ruta)
        archivoLeido = open(ruta, "r")                    #extraer el contenido del archivo con saltos de línea
        archivoLFP = archivoLeido.readlines()             #separar en lista cada salto de línea
        archivoLeido.close()
        archivoCargado = True
        procesarArchivo()
    else:
        print("No se cargo el archivo")
        archivoCargado = False

def procesarArchivo():
    global archivoLFP, curso, parametros, alumnos
    curso = archivoLFP[0].replace("{", "")
    print("Curso: " + curso)
    parametros = archivoLFP[len(archivoLFP)-1].replace("}","")
    print("Paramétros: " + parametros)
    print("Estudiantes: ")
    for x in range(1,len(archivoLFP)-2):
        alumnos.append(archivoLFP[x]) 
    print(alumnos)


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