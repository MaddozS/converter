from check_number import checkNumber
from groups import NUMBER_BASE

def decimalToAnyBase(number, baseNumber):
    if not number or not baseNumber:
        return False

    group = NUMBER_BASE[10]
    int_number = int(number)
    if checkNumber(str(number), group) and baseNumber != 10:
        result = ""
        while int_number != 0:
            res = int_number%int(baseNumber)
            int_number = int_number//int(baseNumber)
            digit = [key for key, value in NUMBER_BASE[baseNumber].items() if value == res][0]
            result += digit

        return result[::-1]

    elif baseNumber == 10:
        return int_number
    else:
        return False