# El proposito de este archivo es mantener ordenado
# el digito que tiene la base con su respectivo valor
# este tiene más sentido en bases mayores a 10, pues
# estos usan otros caracteres además del 0 al 9

BINARY = {
    "0": 0,
    "1": 1
}

BASE_3 = {
    "0": 0,
    "1": 1,
    "2": 2
}
BASE_4 = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3
}
BASE_5 = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4
}
BASE_6 = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5
}
BASE_7 = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6
}
OCTAL = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7
}
BASE_9 = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8
}
DECIMAL = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}
HEXADECIMAL = {
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
NUMBER_BASE = {
    2: BINARY,
    3: BASE_3,
    4: BASE_4,
    5: BASE_5,
    6: BASE_6,
    7: BASE_7,
    8: OCTAL,
    9: BASE_9,
    10: DECIMAL,
    16: HEXADECIMAL
}