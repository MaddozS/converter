def checkNumber(number, dictionary):
    for digit in number:
        if digit not in dictionary:
            return False
    return True