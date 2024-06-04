numero = int(input('Pon un numero entre el 1 y 10:'))

def tabla_multiplicar(numero):
    '''Funcion para realizar la tabla de multiplicador de un numero
    
    parametros:
    numero= el numero dado
    
    salida:
    guardar tabla de multiplicar en un fichero
    y dar la tabla de multiplicar del numero'''

    if numero <=10 and numero>0:
        file ='Tabla_multiplicar' + str(numero) + '.txt'
        x = open(file,'w')

        for i in range (1,11):
            y = numero * i
            print(y)
            x.write(str(y) + '\n')
    else:
        print('no cumple la condicion dada')
    
tabla_multiplicar(numero)