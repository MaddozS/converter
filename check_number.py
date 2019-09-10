# Esta funcion verifica que cada digito
# de nuestro numero se encuentre dentro
# de la base a converitr
def checkNumber(number, dictionary):
    for digit in number:
        if digit not in dictionary:
            return False
    return True