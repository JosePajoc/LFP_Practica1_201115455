from tkinter import filedialog                                  #libreria para entorno gráfico
from io import open                                             #lectura del archivo
import webbrowser                                               #Abrir navegador web
from alumnos import estudiante

opcion = 0
gano = 0 
perdio = 0
promedio = 0
ruta = ""
archivoCargado = False
archivoLFP = []                                                 #Lista para cada línea del archivo
curso = ""
parametros = ""
alumnos = []                                                    #Lista de objetos estudiantes
listaParametros = []

def separador():
    print("-------------------------------------------------------------------------------------")

def cargarArchivo():
    global ruta, archivoCargado, archivoLFP                     #Llamando variables globales
    ruta = filedialog.askopenfilename(title="Seleccionar archivo flp")
    if ruta!="":
        print("Se ha cargado con éxito el archivo \nLa ruta es: " + ruta)
        archivoLeido = open(ruta, "r")                          #extraer el contenido del archivo con saltos de línea
        archivoLFP = archivoLeido.readlines()                   #separar en lista cada salto de línea
        archivoLeido.close()
        procesarArchivo()
    else:
        print("No se cargo el archivo")
        archivoCargado = False

def procesarArchivo():
    global archivoLFP, curso, parametros, alumnos, archivoCargado, listaParametros
    
    curso1 = archivoLFP[0].replace(" = {", "")
    curso = curso1.replace("\n", "")
    
    parametros = archivoLFP[len(archivoLFP)-1].replace("} ","")
    listaParametros = parametros.split(", ")
    
    for x in range(1,len(archivoLFP)-1):        
        temporal = archivoLFP[x].split(";")                     #Lista temporal de estudiantes
        #Depurando nombres
        nombre = temporal[0].replace("\t<", "")
        nombre1 = nombre.replace("<", "")
        nombre2 = nombre1.replace("\"", "")
        #Depurando notas
        nota = temporal[1].replace(">,\n", "")
        nota1 = nota.replace(">, \n", "")
        nota2 = nota1.replace(">", "")
        nota3 = nota2.replace("\n", "")
        #Agregando a la lista de objetos
        alumnos.append(estudiante(nombre2, float(nota3))) 
    archivoCargado = True

def ascendenteNotas():
    global alumnos
    #La lista de objetos se ordena en forma ascendente siempre
    for i in range(len(alumnos)):
        for j in range(len(alumnos) - 1):
            if alumnos[j].verNota() > alumnos[j+1].verNota():
                temp = alumnos[j+1]
                alumnos[j+1] = alumnos[j]
                alumnos[j] = temp

def descendenteNotas():
    global alumnos                                              #Solo se recorre la lista de atrás hacia adelante
    tamano = len(alumnos)
    for i in range(tamano-1, -1, -1):
        print(alumnos[i].verNombre())
        print(alumnos[i].verNota())

def ganoPerdioPromedio():
    global gano, perdio, promedio
    cantidad = 0
    suma = 0
    for i in range(len(alumnos)):
        if alumnos[i].verNota() >= 60:
            gano = gano + 1
        else:
            perdio = perdio + 1
        suma = suma + alumnos[i].verNota()
        cantidad = cantidad + 1
    promedio = suma / cantidad


def mostrarConsola():
    global curso, parametros,alumnos, gano, perdio, promedio, listaParametros

    ascendenteNotas()
    ganoPerdioPromedio()

    separador()
    print("Curso: " + curso)
    separador()
    print("Total de estudiantes: " + str(len(alumnos)))
    separador()
    print("Paramétros: ")
    print(listaParametros)
    
    for i in range(len(listaParametros)):
        if listaParametros[i].upper() == "ASC":
            separador()
            print("Estudiantes: ")
            for i in range(len(alumnos)):
                print(alumnos[i].verNombre())
                print(alumnos[i].verNota())
        elif listaParametros[i].upper() == "DESC":
            separador()
            descendenteNotas()
        elif listaParametros[i].upper() == "AVG":
            separador()
            print('Promedio: ' + str(promedio))
        elif listaParametros[i].upper() == "MIN":
            separador()
            print("Nota mínima, alumno: " + alumnos[0].verNombre() + " Nota: " + str(alumnos[0].verNota()))
        elif listaParametros[i].upper() == "MAX":
            separador()
            print("Nota máxima, alumno: " + alumnos[len(alumnos)-1].verNombre() + " Nota: " + str(alumnos[len(alumnos)-1].verNota()))
        elif listaParametros[i].upper() == "APR":
            separador()
            print('Total de aprobados: ' + str(gano))
        elif listaParametros[i].upper() == "REP":
            separador()
            print('Total de reaprobados: ' + str(perdio))


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
    elif opcion == 2:
        if archivoCargado:
            mostrarConsola()
        else:
            print("Aún no se han cargado datos al sistema...")