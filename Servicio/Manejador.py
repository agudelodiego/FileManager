'''
REALIZADO POR: Diego Alexander Agudelo Garcia
FECHA: 4/Oct/2021

UTILIDAD: El presente archivo enfoca en la creacion de un programa capaz de manejar los archivos de un determinado directorio. Dicho programa se encargara de crear y borrar archivos, listar los archivos del directorio seleccionado, ademas de que se encargara tambien de borrar arcivos
'''

#Importamos el modulo os necesario para el programa
import os


path = 'D:/Programacion/Python/Proyectos/Proyecto2/Servicio/Archivos/'

#------------------Crear archivos----------------- 
def Crear(nombre):

    archivo = path + nombre

    try:

        archivo = open(archivo,'x')
        print(f'''
        El archivo {nombre} fue creado de manera exitosa
        ''')
        listaArchivos.append(nombre)
        return archivo

    except FileExistsError:

        print(f'''
        ******************ERROR******************
        El archivo {nombre} ya existe dentro 
        del directorio, intentalo de nuevo
        usando un nombre diferente
        ''')

    except Exception as error:

        print(f'''
        Algo salio mal creando el archivo {nombre}
        Descripcion del error:{error}
        ERROR: {type(error)}
        ''')
#-------------------------------------------------


#-------------------Leer archivo------------------
def Leer(nombre):

    archivo = path + nombre

    try:

        archivo = open(archivo,'r')
        print('''
        -------------------Leyendo archivo---------------------
        ''')    
        print(f'{archivo.read()}')
        print('')

    except FileNotFoundError:

        print(f'''
        *************************ERROR***********************
        El archivo {nombre} no se encuentra dentro de este
        directorio, intentelo de nuevo
        ''')
    
    except Exception as error:

        print(f'''
        Algo ha salido mal leyendo el archivo {nombre}
        Descripcion del error: {error}
        Nombre error: {type(error)}''')
#-------------------------------------------------


#------------Escribir sobre el archivo------------
def Escribir(nombre,mensaje):

    archivo = path + nombre

    try:

        archivo = open(archivo,'a')
        archivo.write(mensaje)
        print('-------Mensaje anexado exitosamente--------')

    except Exception as error:
        print(f'''
        Algo salio mal escribiendo los dato a {nombre}
        Descripcion del error: {error}
        ERROR: {type(error)}''')
#-------------------------------------------------


#------------------Cerrar archivo-----------------
def Cerrar(archivo):

    try:

        archivo.close()
        print('''
        -----------------Archivo cerrado----------------
        ''')

    except Exception as error:
        print(f'''
        Algo salio cerrando el archivo
        Descripcion del error: {error}
        ERROR: {type(error)}''')
#-------------------------------------------------


#-----------Listar Archivos existentes------------
def Mostrar():

    print('''
    ----------Mostrando lista de archivos existentes--------''')
    for archivo in os.listdir(path):
        print(f'Nombre del archivo --> {archivo}')
#-------------------------------------------------


#-------------------Borrar archivos-----------------
def Borrar(nombre):

    archivo = path + nombre

    try:

        os.remove(archivo)
        print(f'''
        ------------Archivo {nombre} borrado exitosamente
        ''')
    
    except Exception as error:

        print(f'''
        Algo salio mal al intentar borrar el archivo {nombre}
        Descripcion del error: {error}
        ERROR: {type(error)}''')
#---------------------------------------------------



#! ENTRONO DE PRUEBAS
if __name__ == '__main__':

    #Creacion de un archivo
    MiArchivo = Crear('Prueba3.txt')

    #Verificamos que el archivo se haya creado correctamente
    print(type(MiArchivo))

    #Escribimos algo en el archivo 
    sms = '''
    Hola mundo, me presento, soy Diego, soy un programador
    y este es mi primer programa manejador de archivos con 
    python
    '''
    Escribir('Prueba3.txt',sms)

    #Leemos el archivo
    Leer('Prueba3.txt')

    #Volvemos a escribir sobre el archivo 
    sms='Hola, esto es otro ejemplo'
    Escribir('Prueba3.txt',sms)

    #Leemos archivo nuevamente
    Leer('Prueba3.txt')

    #Cerramos el archivo
    Cerrar(MiArchivo)

    #Listamos los archivos existentes
    Mostrar()


    #Borramos un archivo
    Borrar('Prueba2.txt')