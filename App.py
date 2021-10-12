'''
REALIZADO POR: Diego Alexander Agudelo Garcia
FECHA: 05/Oct/2021

FINALIDAD: El presente archivo tiene como objetivo diseñar el codigo para el programa encargado de interactuar con el usuario, dicho programa sera la interfaz que comunique el Programa Catalogo.py con el usuario. Este programa constara de dos funciones, una se llamara programa1 y la otra programa2
'''


#Importamos los modulos necesarios
from Servicio.Catalogo import *




#-----------------Funcion progrma 1-------------------
def Programa1():

    while True:

        print('')
        print('BIENVENIDO'.center(90,'*'))
        print('')
        
        opcion = input('''
        Las opciones que podra elegir son las siguientes:

            M --> Mostrar los archivos del repositorio de trabajo
            C --> Crear archivo nuevos dentro del directorio
            A --> Abir un archivo existente del directorio
            B --> Borrar un archivo
            S --> Salir del programa

        INTRODUZCA LA OPCION SELECCIONADA: ''') 

        if opcion == 'M':
            Catalogo.Mostrar()
        
        elif opcion == 'C':
            
            while True:
                nombre = input('''
                Introduzca el nombre del archivo que desea crear o introduzca la palabra salir para volver al programa principal: ''')

                if nombre == 'salir':
                    print('')
                    print('')
                    print('REGRESANDO AL PROGRAMA PRINCIPAL'.center(90,'*'))
                    print('Por favor espere ...'.center(90))
                    print('')
                    break

                variable = Catalogo.Crear(nombre)

                if variable != False:
                    break

        elif opcion == 'A':
            
            while True:
                nombre = input('''
                Introduzca el nombre del archivo que desea abrir o introduzca la palabra salir para volve al menu principal: ''')

                if nombre == 'salir':
                    print('')
                    print('')
                    print('VOLVIENDO AL PROGRAMA PRINCIPAL'.center(90,'*'))
                    print('')
                    break

                validacion = Catalogo.Verificar(nombre)

                if validacion == True:
                    print('')
                    print('Abriendo el archivo'.center(90))
                    print('Por favor espere...'.center(90))
                    print('')
                    programa2(nombre)
                    break

                elif validacion == False:

                    print('''


                    El archivo seleccionado no existe o no se encuentra dentro
                    del directorio de trabajo
                    
                    
                    ''')

        elif opcion == 'B':

            while True:

                nombre = input('''
                Introduzca el nombre del archivo que desa borrar o introduzca salir para volver al menu pricipal: ''')

                if nombre == 'salir':
                    print('')
                    print('')
                    print('Volviendo al menu principal'.center(90,'*'))
                    print('Por favor espere...'.center(90))
                    break

                variable = Catalogo.Borrar(nombre)

                if variable == True:
                    break
                else:
                    print('''
                    Vuelva a intentarlo''')

        elif opcion == 'S':
            print('''
            
            
            
            
            ''')
            print('Gracias por usar nuestro programa'.center(90,'*'))
            print('Vuelva a pronto'.center(90,'*'))
            print('EL PROGRAMA HA FINALIZADO'.center(90),'*')
            print('''
            
            
            
            ''')
            break 
#-----------------------------------------------------


#----------------Funcion programa 2-------------------
def programa2(nombre):
    
    while True:

        print('')
        print(f'Ustede se encuentra dentro del archivo {nombre}'.center(80,'-'))
        print('')

        accion = input('''
        Las acciones que ud podra realizar con el archivo son las siguiente:
            L --> Leer el archivo
            M --> Modificar el archivo
            S --> Para volver al menu pricipal
        Introduzca la opcion seleccionada: ''')

        if accion == 'L':
            Catalogo.Leer(nombre)
        
        elif accion == 'M':
            mensaje = input('''
            Introduzca la informacion que desea agregar: ''')
            Catalogo.Escribir(nombre,mensaje)

        elif accion == 'S':
            print('''
            
            
            ''')
            print('VOLVIENDO AL MENU PRINCIPAL'.center(90,'*'))
            print('Por favor espere'.center(90,'*'))
            print('''
            
            
            ''')
            break
#-----------------------------------------------------
Programa1()