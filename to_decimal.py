from check_number import checkNumber
from groups import NUMBER_BASE

def anyBaseToDecimal(number, baseNumber):
    if not number or not baseNumber:
        return False
    group = NUMBER_BASE[baseNumber]
    if checkNumber(str(number), group):
        i = 0
        decimal = 0
        for digit in str(number)[::-1]:
            decimal += group[digit]*(int(baseNumber)**i)
            i += 1
        return decimal
    else:
        return False