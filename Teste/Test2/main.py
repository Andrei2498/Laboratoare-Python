def prime(n):
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True


def problema4(my_list):
    new_list = []
    for i in my_list:
        if isinstance(i, int):
            new_list.append(i)
    new_list.sort(reverse=True)
    return new_list


def problema3(m):
    new_list=[]
    for i in range(2, m):
        if prime(i):
            new_list.append(i)
    new_list.sort()
    return  new_list


print(problema4([1, 2, 'trei', 4, [5, 6]]))
print(problema3(5))