# x = [1, 2, -1, 0]
# print(any((i < 0 for i in x)))
# print(list(enumerate(x)))
# x = [(1, 2), (3, 0), (4, 6)]
# print(sorted(x, key=lambda i: i[1] - i[0]))
# it = [1, 2, 4, 7, 5]
# filter(lambda x: bool(x % 2), it) #f poate fi orice functie, si lambda

# x = [1, 2, 3]
# y = [3, 2, 1]
# print(list(zip(x, y))) #returneaza generator si perechile (1,3) (2,2) (3,1)

#map(f, it) returneaza un generator
# x = [1, 2, 3, 4, 5]
# print(list(map(lambda i: i*i, x)))
#map(f, it1, it2, ...) f trebuie sa aiba acelasi nr de parametri ca nr de functii
# it1 = [1, 2, 3]
# it2 = [7, 8, 9]
# print(list(map(lambda a, b: a+b, it1, it2)))

# def problem1(my_list):
#     even_list = []
#     odd_list = []
#     for i in my_list:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     return list(zip(even_list, odd_list))


#Versiunea pe o linie
def problem1(my_list):
    return list(zip( filter(lambda x: x % 2 == 0, my_list), filter(lambda x: x % 2 == 1, my_list)))


# def problem2(pairs):
#     list_dictionary = []
#     for i in pairs:
#         dictionary = {'sum': i[0]+i[1],'prod': i[0]*i[1],'pow': i[0]**i[1]}
#         list_dictionary.append(dictionary)
#     return list_dictionary


#Versiunea pe o linie
def problem2(pairs):
    return list(map(lambda x: {'sum': x[0]+x[1], 'prod': x[0]*x[1], 'pow': x[0]**x[1]}, pairs))


print(problem2(	[(2, 3), (5, 6)]))

