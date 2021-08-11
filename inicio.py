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
repConsola = False

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
    global curso, parametros,alumnos, gano, perdio, promedio, listaParametros, repConsola

    ascendenteNotas()
    ganoPerdioPromedio()
    repConsola = True
    
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

def mostrarReporteHTML():
    global curso, parametros,alumnos, gano, perdio, promedio, listaParametros, repConsola
    
    if repConsola == False:
        ascendenteNotas()
        ganoPerdioPromedio()
    
    archivoCSS = open("estilos.css", "w")
    contenidoCSS = """html {   font-size: 20px; font-family: 'Open Sans', sans-serif; } \n
                    h1 { font-size: 60px; text-align: center; } \n
                    p, li {   font-size: 16px;   line-height: 2;   letter-spacing: 1px; }\n
                    html { background-color: #00539F; }
                    body { width: 1100px; margin: 0 auto; background-color: #FF9500; padding: 0 20px 20px 20px; border: 5px solid black; }
                    h1 { margin: 0; padding: 20px 0; color: #00539F; text-shadow: 3px 3px 1px black; }"""
    archivoCSS.write(contenidoCSS)
    archivoCSS.close()

    archivoHTML = open("index.html", "w")
    archivoHTML.write("\n<!Doctype html>")
    archivoHTML.write("\n<html>")
    archivoHTML.write("\n<head>")
    archivoHTML.write("\n<title>Practica 1 - LFP</title>")
    archivoHTML.write('\n<link href="estilos.css" rel="stylesheet" type="text/css">')
    archivoHTML.write("\n</head>")
    archivoHTML.write("\n<body>")
    archivoHTML.write("\n<h1>Curso: " + curso + "</h1>")
    archivoHTML.write("\n<hr>")

    archivoHTML.write("\nTotal de estudiantes: " + str(len(alumnos)))
    archivoHTML.write("\n<hr>")
    archivoHTML.write("\nParamétros: " +  ", ".join(listaParametros))
    archivoHTML.write("\n<hr>")

    archivoHTML.write("\n<h2>Listado general de estudiantes</h2>")
    archivoHTML.write("\n<table border = \"1\">")
    archivoHTML.write("\n<tr>")
    archivoHTML.write("\n\t<td>")
    archivoHTML.write("\n\t\tEstudiante")
    archivoHTML.write("\n\t</td>")
    archivoHTML.write("\n\t<td>")
    archivoHTML.write("\n\t\tNota")
    archivoHTML.write("\n\t</td>")
    for x in range(len(alumnos)):
        archivoHTML.write("\n\t<tr>")
        archivoHTML.write("\n\t\t<td>")
        archivoHTML.write("\n\t\t" + alumnos[x].verNombre())
        archivoHTML.write("\n\t\t</td>")
        archivoHTML.write("\n\t\t<td>")
        if alumnos[x].verNota()>=60:
            archivoHTML.write("\n\t\t<font color=\"#0000ff\">" + str(alumnos[x].verNota()) + "</font>")
        else:
            archivoHTML.write("\n\t\t<font color=\"#ff0000\">" + str(alumnos[x].verNota()) + "</font>")
        archivoHTML.write("\n\t\t</td>")
        archivoHTML.write("\n\t</tr>")
    archivoHTML.write("\n</tr>")
    archivoHTML.write("\n</table>")
    
    for i in range(len(listaParametros)):
        if listaParametros[i].upper() == "ASC":
            archivoHTML.write("\n<hr>")
            archivoHTML.write("\nEstudiantes en orden ascendente")
            archivoHTML.write("\n<ul>")
            for i in range(len(alumnos)):
                archivoHTML.write("\n<li>" + alumnos[i].verNombre() + ", "+ str(alumnos[i].verNota()) + "</li>")
            archivoHTML.write("\n</ul>")    
        elif listaParametros[i].upper() == "DESC":
            archivoHTML.write("\n<hr>")
            tamano = len(alumnos)
            archivoHTML.write("\nEstudiantes en orden descendente")
            archivoHTML.write("\n<ul>")
            for i in range(tamano-1, -1, -1):
                archivoHTML.write("\n<li>" + alumnos[i].verNombre() + ", "+ str(alumnos[i].verNota()) + "</li>")
            archivoHTML.write("\n</ul>")
        elif listaParametros[i].upper() == "AVG":
            archivoHTML.write("\n<hr>")
            archivoHTML.write('Promedio: ' + str(promedio))
        elif listaParametros[i].upper() == "MIN":
            archivoHTML.write("\n<hr>")
            archivoHTML.write("Nota mínima, alumno: " + alumnos[0].verNombre() + " Nota: " + str(alumnos[0].verNota()))
        elif listaParametros[i].upper() == "MAX":
            archivoHTML.write("\n<hr>")
            archivoHTML.write("Nota máxima, alumno: " + alumnos[len(alumnos)-1].verNombre() + " Nota: " + str(alumnos[len(alumnos)-1].verNota()))
        elif listaParametros[i].upper() == "APR":
            archivoHTML.write("\n<hr>")
            archivoHTML.write('Total de aprobados: ' + str(gano))
        elif listaParametros[i].upper() == "REP":
            archivoHTML.write("\n<hr>")
            archivoHTML.write('Total de reaprobados: ' + str(perdio))
            
    archivoHTML.write("\n</body>")
    archivoHTML.write("\n</html>")
    archivoHTML.close()
    print("Se ha creado con éxito el reporte HTML...")
    webbrowser.open_new_tab("index.html")

#----------------------------------------Menú principal----------------------------------------------
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
    elif opcion == 3:
        if archivoCargado:
            mostrarReporteHTML()
        else:
            print("Aún no se han cargado datos al sistema...")