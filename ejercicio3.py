import os
n = int(input('Pon un numero entre el 1 y 10:'))
m = int(input('Pon un numero entre el 1 y 10:'))

def buscar_linea(n,m):
    '''funcion para encontrar la linea de la tabla de multiplicar
    
    parametros:
    n = numero que sera la tabla de mutlipicar
    m = la linea que queremos de la tabla
     
    salida:
     La tabla de multiplicar del numero con la linea correspondiente '''

    buscar = os.path.isfile('Tabla_multiplicar' + str(n) + '.txt')
    
    if buscar == True:
        file = open('Tabla_multiplicar' + str(n) + '.txt','r')
        lineas = file.readlines()
        print(lineas[m-1])
    else:
        print('no se encontro el archivo')

buscar_linea(n,m)