from check_number import checkNumber
from groups import NUMBER_BASE

def decimalToAnyBase(number, baseNumber):
    # Revisa si los parametros de number y baseNumber no estás vacíos
    if not number or not baseNumber:
        return False
    
    # Aseguramos que nuestras entradas sean numeros enteros.
    int_baseNumber = int(baseNumber)
    int_number = int(number)

    # Nuestra base debe estar dentro de las bases ya registradas en
    # el archivo groups.py
    if int_baseNumber not in NUMBER_BASE:
        return False
    
    # Como la base del numero inicial ya es 10, entonces asignamos
    # directamente el diccionario de los números que conforman esta
    # base
    group = NUMBER_BASE[10]

    # Condicional que verifica si cada caracter de nuestro numero a 
    # convertir se encuentra dentro del conjunto de los numeros de
    # la base10.
    if checkNumber(str(number), group):
        result = ""
        # Hacemos un ciclo hasta que el numero inicial hasta que
        # este sea igual a 0
        while int_number != 0:
            # Obtenemos el resultado del modulo del numero inicial 
            # con la base a la que lo queremos convertir, en este caso
            # aseguramos que este sea un numero entero.
            res = int_number%int_baseNumber
            # Realizamos la division entre el numero inicial y la base,
            # la notacion de // es para indicial una division entera, es
            # decir, no dará puntos decimales
            int_number = int_number//int_baseNumber
            # Buscamos al digito al cual nuestro resultado del residuo está asignado,
            # por ejemplo, si obtenemos un 6 y queremos convertir en base 7,
            # este iterará nuestro diccionario en dos valores (la llave y el valor) y
            # únicamente asignará la llava la cual tenga de valor nuestro residuo (la
            # llave es el digito).
            # Ahora, como este se asigna a un arreglo, como es un arreglo de un digito,
            # con [0] lo obtenemos
            digit = [key for key, value in NUMBER_BASE[int_baseNumber].items() if value == res][0]
            result += digit
        # Como nuestra cadena de nuestra conversión de armó de manera inversa,
        # este se debe retornar de manera inversa, con Python se puede usar
        # esta notación para hacerlo ([::-1])
        return result[::-1]

    else:
        return False