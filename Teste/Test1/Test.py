def problema1(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma


def problema5(n):
    number = str(int(n, 8))
    if number == number[:: -1]:
        return True
    else:
        return False


print(problema1(199))
print(problema5("10"))