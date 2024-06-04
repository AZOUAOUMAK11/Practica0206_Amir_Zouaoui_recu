import os
n = int(input('Pon un numero entre el 1 y 10:'))

def leer_ficheros(numero):
    '''Funcion para encontrar tabla de multiplicar del numero si hay
    
    parametros:
    n= el numero dado
    
    salida:
    la tabla de multiplicar del numero o decir que no se encuentra'''

    buscar = os.path.isfile('Tabla_multiplicar' + str(numero) + '.txt')
    
    if buscar == True:
        file = open('Tabla_multiplicar' + str(numero) + '.txt','r')
        Tabla_multiplicar = file.read()
        print(Tabla_multiplicar)
    else:
        print('no se encontro el archivo')

leer_ficheros(n)