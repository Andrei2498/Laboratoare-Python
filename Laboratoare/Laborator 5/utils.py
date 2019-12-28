def check_if_prime(number):
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return False
    return True


def process_item(x):
    while True:
        x += 1
        if check_if_prime(x):
            return x




