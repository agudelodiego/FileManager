'''
REALIZADO POR: Diego Alexander Agudelo Garcia
FECHA: 4/Oct/2021

UTILIDAD: El presente archivo esta dedicado para la creacion de un clase llamada peliculas, la cual estara encarda de representar una pelicula, la cual posteriorente sera agregada a un archivo llamado catalogo.txt
'''

#Creacion de la clase
class Pelicula:

    #-----------------Metodo constructor------------------
    def __init__(self,nombre,genero,director,estreno):
        self._nombre = nombre
        self._genero = genero
        self._director = director
        self._estreno = estreno
    #-----------------------------------------------------


    #---------GET y SET para nombre---------
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nuevo):
        self._nombre = nuevo
    #--------------------------------------


    #-------GET y SET para genero----------
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self,nuevo):
        self._genero = nuevo
    #--------------------------------------


    #------GET y SET para director---------
    @property
    def director(self):
        return self._director

    @director.setter
    def director(self,nuevo):
        self._director = nuevo
    #--------------------------------------


    #------GET y SET para estreno----------
    @property
    def estreno(self):
        return self._estreno

    @estreno.setter
    def estreno(self,nuevo):
        self._estreno = nuevo
    #--------------------------------------


    #----------Metodo __str__ -------------
    def __str__(self):
        mensaje = f'''INFORMACION
        NOMBRE PELICULA: {self._nombre}
        GENERO: {self._genero}
        DIRECTOR: {self._director}
        ESTRENO: {self._estreno}
        '''
        return mensaje
    #--------------------------------------



#!---------------ENTORNO DE PRUEBAS-----------------
if __name__ == '__main__':
    
    #Instanciamiento de clase peliculas
    peli1 = Pelicula('Son como niños','Comedia','Adam Samdler','2009')
    peli2 = Pelicula('Live, vida inteligente','Ciencia ficcion','Su madre','2014')
    peli3 = Pelicula('El juego de Ender','Ciencia ficcion/Fantasia','Su pudra madre','2019')

    #Uso de metodo nombre
    peli1.nombre = 'Nuevo nombre'
    print('Nombre de la pelicula -->',peli1.nombre)

    #Uso de metodo genero
    peli2.genero = 'Intercambio'
    print('Genero de la pelicual -->',peli2.genero)

    #Uso de metodo director
    peli3.director = 'Fui yo, ome, pedazo de hijuputa, ome, ome'
    print('Director de la pelicula -->',peli3.director)

    #Uso de metodo estreno
    peli3.estreno = 'Nueva fecha'
    print('Fecha de estreno -->',peli3.estreno)

    #Uso de metodo __str__
    print(peli2)
#!--------------------------------------------------