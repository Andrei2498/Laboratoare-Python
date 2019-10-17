# Exercitiul 1

# fibonacci_list = []
#
#
# def fibonacci(n):
#     if n == 1:
#         fibonacci_list.append(0)
#     elif n == 2:
#         fibonacci_list.append(0)
#         fibonacci_list.append(1)
#     else:
#         a = 0
#         b = 1
#         fibonacci_list.append(0)
#         fibonacci_list.append(1)
#         while n > 2:
#             aux = a
#             a = b
#             b = b + aux
#             fibonacci_list.append(b)
#             n = n - 1
#     print(fibonacci_list)
#
#
# fibonacci(int(input()))

# Exercitiul 2

# import math
#
#
# def is_prime(n):
#     for i in range(2, math.floor(n / 2 + 1)):
#         if n % i == 0:
#             return False
#     return True
#
#
# print(is_prime(int(input())))

# Exercitiul 3

# import random
#
#
# def find_line_coords(points_list):
#     for i in points_list:
#         a = random.randint(-10, 10)
#         b = random.randint(-10, 10)
#         coords = i.split(',')
#         c = - (a * int(coords[0]) + b * int(coords[1]))
#         print('(' + str(a) + ',' + str(b) + ',' + str(c) + ') ', end="")
#
#
# find_line_coords(input().split())

# Exercitiul 4


# def list_operations(first_set, second_set):
#     return first_set | second_set, first_set & second_set, first_set - second_set, second_set-first_set
#
#
# a = input().split()
# b = input().split()
# print(list_operations(set(a), set(b)))

# Exercitiul 5

# from itertools import combinations
#
#
# list_from_input = input().split()
# k = input()

# Next 2 lines will convert the str list into integer list
# for i in range(0, len(list_from_input)):
#     list_from_input[i] = int(list_from_input[i])

# print(list(combinations(list_from_input, int(k))))

# Exercitiul 6

# def find_chars_with_x_appearances(x, *args):
#     full_list = []
#     for i in range(0, len(args)):
#         full_list += args[i]
#     unique_list = set(full_list)
#     for i in unique_list:
#         if full_list.count(i) == x:
#             print(str(i) + " ", end="")
#
#
# find_chars_with_x_appearances(2, [1, 2, 3], [3, 4, 5], [4, 5, 8])

# Exercitiul 7

# def ascii_problem(x=1, *strings, flag=True):
#     list_of_elements = list(strings)
#     for i in range(0,len(list_of_elements) - 1):
#         string = list_of_elements[i]
#         char_list = []
#         if flag:
#             for j in string:
#                 if ord(j) % x:
#                     char_list.append(j)
#         else:
#             for j in string:
#                 if not ord(j) % x:
#                     char_list.append(j)
#         list_of_elements[i] = char_list
#     del list_of_elements[-1]
#     return list_of_elements
#
#
# print(ascii_problem(2, "test", "hello", "lab002", False))

# Exercitiul 8

# def list_to_tuple(*lists):
# #     new_list = []
# #     max_length = len(max(lists, key=len))
# #     for i in lists:
# #         if len(i) < max_length:
# #             while not len(i) == max_length:
# #                 i += [None]
# #         new_list += i
# #     k = 0
# #     print(new_list)
# #     while k < len(lists):
# #         for j in range(0, len(lists)):
# #             aux = new_list[(4*j+4)]
# #             new_list[(4*j+4)] = new_list[j]
# #             new_list[j] = new_list[aux]
# #         k += 1
# #     print(new_list)
# #
# #
# # list_to_tuple([1, 2, 3], [3, 5, 6], [2, 3])


# Exercitiul 9


# def sort_tuple(list_of_tuples):
#     length = len(list_of_tuples)
#     for i in range(0, length):
#         for j in range(0,length-i-1):
#             if list_of_tuples[j][1][2] > list_of_tuples[j + 1][1][2]:
#                 aux = list_of_tuples[j]
#                 list_of_tuples[j] = list_of_tuples[j + 1]
#                 list_of_tuples[j + 1] = aux
#     print(list_of_tuples)
#
#
# sort_tuple([('abc', 'bcd'), ('abc', 'zza'), ('adc', 'adb')])

# x = {1:2, 3:5}
# for el in x.items():
#     print(el[1])

# Test 1

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


