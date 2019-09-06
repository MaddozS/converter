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
    hexa_dict = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }

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
    

# print(hexa_to_decimal("FFFF"))
print(binary_to_decimal("100101"))
print(decimal_to_binary(37))
print(any_to_decimal("binary", "100101"))