# Conventer any binary based number to any other base
import groups
from check_number import checkNumber

def binaryToDecimal(x):
    if checkNumber(x, groups.BINARY) is True:
        i = 0
        decimal = 0
        for a in x[::-1]: # This notation inverts the string
            decimal += int(a)*(2**i)
            i += 1
        return decimal
    else:
        return 'Invalid input, check it'

print(binaryToDecimal('101'))

def divideString(binaryNumber, maxDigits):
    while len(binaryNumber)%maxDigits != 0:
        binaryNumber = "".join(["0",binaryNumber])
    parts = [binaryNumber[i:i+maxDigits] for i in range(0, len(binaryNumber), maxDigits)]
    return parts

def binaryToBase3(x):
    if checkNumber(x, groups.BINARY) is True:
        xDecimal = binaryToDecimal(x)
        result = ""
        while xDecimal != 0:
            res = xDecimal % 3
            xDecimal = xDecimal//3
            result += str(res)
        return result[::-1]

    else:
        return 'Invalid input, check it'

def binaryToBase4(x):
    if checkNumber(x, groups.BINARY) is True:
        xBase4 = ""
        pairs = divideString(x, 2)
        for pair in pairs:
            i = 1
            y = 0
            for digit in pair:
                y += int(digit)*(2**i)
                i -= 1
            base4_digit = [key for key, value in groups.BASE_4.items() if value == y ][0]
            xBase4 += base4_digit
        return xBase4
    else:
        return 'Invalid input, check it'

def binaryToBase5(x):
    if checkNumber(x, groups.BINARY) is True:
        xDecimal = binaryToDecimal(x)
        result = ""
        while xDecimal != 0:
            res = xDecimal % 5
            xDecimal = xDecimal//5
            result += str(res)
        return result[::-1]
    else:
        return 'Invalid input, check it'

def binaryToBase6(x):
    if checkNumber(x, groups.BINARY) is True:
        xDecimal = binaryToDecimal(x)
        result = ""
        while xDecimal != 0:
            res = xDecimal % 6
            xDecimal = xDecimal//6
            result += str(res)
        return result[::-1]
    else:
        return 'Invalid input, check it'

def binaryToBase7(x):
    if checkNumber(x, groups.BINARY) is True:
        xDecimal = binaryToDecimal(x)
        result = ""
        while xDecimal != 0:
            res = xDecimal % 7
            xDecimal = xDecimal//7
            result += str(res)
        return result[::-1]
    else:
        return 'Invalid input, check it'
    
def binaryToOctal(x):
    if checkNumber(x, groups.BINARY) is True:
        xOctal = ""
        digitGroups = divideString(x, 3)
        for digitGroup in digitGroups:
            i = 2
            y = 0
            for digit in digitGroup:
                y += int(digit)*(2**i)
                i -= 1
            octal_digit = [key for key, value in groups.OCTAL.items() if value == y ][0]
            xOctal += octalDigit
        return xOctal
    else:
        return 'Invalid input, check it'

print(binaryToBase7('110'))
