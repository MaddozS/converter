from from_decimal import *
from to_decimal import *

base = int(input('Base: '))
number = int(input('number: '))
baseResult = int(input('convert to: '))

x = None
if base == baseResult:
    x = number
elif baseResult == 10:
    x = anyBaseToDecimal(number, base)
elif base == 10:
    x = decimalToAnyBase(number, baseResult)
else:
    xDecimal = anyBaseToDecimal(number, base)
    x = decimalToAnyBase(xDecimal, baseResult)

print(x)