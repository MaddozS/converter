from check_number import checkNumber
from groups import NUMBER_BASE

def anyBaseToDecimal(number, baseNumber):
    # Revisa si los parametros de number y baseNumber no estás vacíos
    if not number or not baseNumber:
        return False

    # Aseguramos que nuestras entradas sean del tipo que que necesitamos
    # que sea.
    str_number = str(number)
    int_baseNumber = int(baseNumber)

    # Nuestra base debe estar dentro de las bases ya registradas en
    # el archivo groups.py
    if int_baseNumber not in NUMBER_BASE:
        return False

    # Obtenemos, mediante el número de la base, el diccionario de
    # los digitos con sus valores de esa base
    group = NUMBER_BASE[baseNumber]

    if checkNumber(str_number, group):
        # Inicializamos nuestro contrador y el valor del numero
        # decimal en 0
        i = 0
        decimal = 0

        # Iteramos cada digito que tiene nuestra cadena de nuestro
        # numero a convertir, en este caso, la cadena se invierte
        # para empezar con los digitos de la izquierda
        for digit in str_number[::-1]:
            # A nuestro número decimal le iremos sumando el valor
            # que tenga el digito de nuestro numero multiplicado 
            # por el valor de su posición, por ejemplo, si tenemos
            # A en hexadecimal, este se ingresará como llave de 
            # nuestro diccionario y obtendremos el número 10, luego,
            # multiplicaremos ese numero por 16^0, en este caso será
            # 0, pues está en esa posición, este se sumará a decimal
            # se retornará, dando 10.
            decimal += group[digit]*(int_baseNumber**i)
            i += 1
        return decimal
    else:
        return False