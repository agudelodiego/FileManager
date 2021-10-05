'''
REALIZADO POR: Diego Alexander Agudelo Garcia

FECHA: 5/Oct/2021

FINALIDAD: El presente documento esta enfocado en la creacion de una clase que se encargue de manejar los recursos de la aplicacion, dicha clase se llamara Catalogo y sera la encargada de borrar y crear archivos, escribir sobre un archivo, listar la cantidad de archivos en el directorio de trabajo, mostrar el contenido de un determinado archivo, asi como abrir y cerrar archivos existentes 
'''


#Importamos el modulo os necesario para el programa
import os


#Creacion de la clase
class Catalogo :

    #Ruta de trabajo
    path = 'D:/Programacion/Python/Proyectos/Proyecto2/Servicio/Archivos/'

    #--------------------Metodo Constructor---------------------
    def __init__(self):
        pass
    #-----------------------------------------------------------


    #--------------------Metodo Crear Archivo-------------------
    @classmethod
    def Crear(cls,nombre):
        archivo = cls.path + nombre

        try:

            archivo = open(archivo,'x')
            print(f'''
            El archivo {nombre} fue creado de manera exitosa
            ''')
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
    #----------------------------------------------------------


    #--------------Metodo escribir sobre un archivo------------
    @classmethod
    def Escribir(cls,nombre,mensaje):

        archivo = cls.path + nombre

        if(os.path.exists(archivo)):

            try:
                archivo = open(archivo,'a')
                archivo.write(mensaje)
                print('-------Mensaje anexado exitosamente--------')

            except Exception as error:
                print(f'''
                Algo salio mal escribiendo los dato a {nombre}
                Descripcion del error: {error}
                ERROR: {type(error)}''')

        else:
            print(f'''
            Error: El archiv {nombre} NO existe dentro del directorio 
            de trabajo, intentelo de nuevo usando un archvio existente
            ''')
    #----------------------------------------------------------


    #-------------------Metodo leer archivos-------------------
    @classmethod
    def Leer(cls,nombre):

        archivo = cls.path + nombre

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
    #----------------------------------------------------------


    #------Mostrar los archivos existentes del directorio------
    @classmethod
    def Mostrar(cls):

        print('''
        ----------Mostrando lista de archivos existentes--------''')
        for archivo in os.listdir(cls.path):
            print(f'Nombre del archivo --> {archivo}')
    #-----------------------------------------------------------


    #------------------Metodo cerrar archivo--------------------
    @classmethod
    def Cerrar(cls,archivo):

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
    #-----------------------------------------------------------


    #---------------------Eliminar archivos---------------------
    @classmethod
    def Borrar(cls,nombre):

        archivo = cls.path + nombre

        try:

            os.remove(archivo)
            print(f'''
            ------------Archivo {nombre} borrado exitosamente
            ''')
    
        except FileNotFoundError:

            print(f'''
            El archivo {nombre} no existe dentro del directorio 
            de trabajo, intentelo de nuevo con un archivo existente
            ''')

        except Exception as error:

            print(f'''
            Algo salio mal al intentar borrar el archivo {nombre}
            Descripcion del error: {error}
            ERROR: {type(error)}''')
    #-----------------------------------------------------------


#!----------------ENTORNO DE PRUEBAS--------------------- 
if __name__ == '__main__':
    
    #--------------Creacion de archivos------------------
    #* Para crear un archivo se usa la clase Catalogo en conjunto con el metodo Crear(parametro), metodo al cual se le debe pasar como parametro el nombre del archivo que se desea crear. Si dicho archivo ya existe dentro del directorio el programa enviara un mensaje de error. Este metodo devuelve el objeto archivo que fue creado
    Archivo1 = Catalogo.Crear('Ejemplo1.txt')
    Archivo2 = Catalogo.Crear('Ejemplo2.txt')
    Archivo3 = Catalogo.Crear('Ejemplo3.txt')
    #----------------------------------------------------



    #-------------Escribir sobre un archivo---------------
    #* Para escribir sobre un archivo se usa el nombre de la clase Catalogo con el metodo Escribir(par1,par2), al cual se le deben de pasar dos parametros, el primero corresponde al nombre del archivo sobre el que se desea escribir, y el segundo es el mensaje o lo que se desea escribir en dicho archivo. Si el archivo seleccionado no existe dentro del directorio de trabajo el programa imprime un mensaje de error
    mensaje1 = '''
    Hola esto es un ejemplo y es puro texto de relleno
    Ya no se que mas poner'''
    mensaje2 = '''
    Hola mundo este es mi primer programa manejador de 
    recursos usando python, esto es un texto de relleno'''
    Catalogo.Escribir('Ejemplo1.txt',mensaje1)
    Catalogo.Escribir('Ejemplo10.txt',mensaje2)
    Catalogo.Escribir('Ejemplo3.txt',mensaje1)
    #-----------------------------------------------------



    #------------------Lectura de archivos----------------
    #* Para leer un archivo que se encuentra dentro del directorio de trabajo se usa la clase Catalogo con el metodo Leer(par), al cual se le debe de pasar un parametro, mismo que corresponde al nombre del archivo que se desea leer. Si el archivo no existe, el programa imprimira un mensaje de error
    Catalogo.Leer('Ejemplo1.txt')
    Catalogo.Leer('Ejemplo3.txt')
    #-----------------------------------------------------



    #--------Mostrar los archivos del directorio----------
    #* Para saber los archivo existenetes dentro del directorio de trabajo se usa la clase Catalogo con el metodo Mostrar(), al cual no se le debe de pasar ningun parametro
    Catalogo.Mostrar()
    #-----------------------------------------------------


    #------------------Cerrar un archivo------------------
    #* Para cerrar un archivo que fue previamente creado se usa el la clase Catalogo y el metodo Cerrar(par), al cual se le debe de pasar como parametro el objeto archivo que devuelve el metodo Crear() de la misma clase
    Catalogo.Cerrar(Archivo1)
    Catalogo.Cerrar(Archivo2)
    Catalogo.Cerrar(Archivo3)
    #-----------------------------------------------------


    #--------------------Borrar un archivo----------------
    #* Para borrar un archivo se usa la clase Catalogo con el metodo Borrar(par), al cual se le debe de pasar como parametro el nombre del archivo que se desea borrar. Si el archivo no existe dentro del directorio de trabajo el programa imprime un error en pantalla. Si el archivo no ha sido previamente cerrado tambien lanzara un error
    Catalogo.Borrar('Ejemplo1.txt')
    Catalogo.Borrar('Ejemplo2.txt')
    Catalogo.Borrar('Ejemplo3.txt')
    Catalogo.Borrar('Ejemplo5.txt')
    #-----------------------------------------------------
#!-------------------------------------------------------

