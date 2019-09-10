HEXA_DICT = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def binary_to_decimal(x):
    i = 0
    decimal = 0
    for a in x[::-1]:
        decimal += int(a)*(2**i)
        i += 1
    return decimal

def octal_to_decimal(x):
    i = 0
    decimal = 0
    for a in x[::-1]:
        decimal += int(a)*(8**i)
        i += 1
    return decimal

def hexa_to_decimal(x):
    i = 0
    decimal = 0

    for a in x[::-1]:
        int_a = None
        if a in hexa_dict:
            int_a = hexa_dict[a]
        else:
            int_a = int(a)

        decimal += int_a*(16**i)
        i += 1
    return decimal

def decimal_to_binary(x):
    str_binary = ""
    while (x != 0):
        res = x%2
        x = x//2
        print(f'{x},{res}')
        str_binary += str(res)
    return str_binary[::-1]

def binary_to_hexa(x):
    str_hexa = ""
    if len(x)%4 != 0:
        while len(x)%4 != 0:
            x = "".join(["0",x])
    parts = [x[i:i+4] for i in range(0, len(x), 4)]
    print(parts)
    for part in parts:
        i = 3
        y=0
        for x in part:
            y += int(x)*(2**i)
            i -=1
        print(y)
        hexa_char = [key for key, value in HEXA_DICT.items() if value == y][0]
        str_hexa += hexa_char
    return str_hexa




def any_to_decimal(base, value):
    str_value = str(value) # Always be an string
    converted = None # The result
    if base == "decimal":
        return str_value
    elif base == "binary":
        converted = binary_to_decimal(str_value)
    elif base == "octal":
        converted = octal_to_decimal(str_value)
    elif base == "hexadecimal":
        converted = hexa_to_decimal(str_value)
    return converted
    
binary_to_hexa("101111")