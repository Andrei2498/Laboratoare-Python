# Exercitiul 2


# def my_function(*args, **kwargs):
#     return sum(kwargs.values())
#
#
# result = lambda *args, **kwargs: sum(kwargs.values())
# print(result(1, 2, c=3, d=4))
# print(my_function(1, 2, c=3, d=4))


# Exercitiul 3

# vowel_list = ['a', 'e', 'i', 'o', 'u']
# string = "Programming in Python is fun"
#
#
# # Function
# def get_vowels():
#     vowels_from_string = []
#     for i in string.lower():
#         if i in vowel_list:
#             vowels_from_string.append(i)
#     return vowels_from_string
#
#
# # List Comprehension
# string_vowels = [i for i in string.lower() if i in vowel_list]
#
#
# # Filter
# def check_if_vowel(character):
#     if character in vowel_list:
#         return True
#     else:
#         return False
#
#
# filtered = list(filter(check_if_vowel, string))
#
#
# # Lambda / Anonymous Function
# def lambda_function():
#     return lambda char: check_if_vowel(char)
#
#
# list_of_vowels = []
# for i in string:
#     result = lambda_function()
#     if result(i):
#         list_of_vowels.append(i)

# Exercitiul 4

# def get_dictionaries(*args, **kwargs):
#     new_list = []
#     for i in args:
#         if type(i) is dict:
#             if len(i) >= 2:
#                 for j in i.items():
#                     if type(j[0]) is str and len(str(j[0])) > 2:
#                         new_list.append(i)
#                         break
#     for i in kwargs.values():
#         if type(i) is dict:
#             if len(i) >= 2:
#                 for j in i.items():
#                     if type(j[0]) is str and len(str(j[0])) > 2:
#                         new_list.append(i)
#     print(new_list)
#
#
# get_dictionaries({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
#                  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True})

# Exercitiul 5

# def get_numbers(list_of_elements):
#     list_of_numbers = []
#     for i in list_of_elements:
#         if type(i) is int or type(i) is float:
#             list_of_numbers.append(i)
#     return list_of_numbers
#
#
# print(get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

# Exercitiul 6

# def make_pairs(first_list, second_list):
#     return first_list, second_list
#
#
# def calculate_line(first_point, second_point):
#     slope = second_point[1]-first_point[1]
#     return str(slope * first_point[0] - first_point[1]), str(- slope) + 'x', str(second_point[0] - first_point[0]) + 'y'
#
#
# def get_lines(list_of_points):
#     list_of_lines = []
#     for i in range(0, len(list_of_points) - 1):
#         for j in range(i + 1, len(list_of_points)):
#             if not list_of_points[i] == list_of_points[j] and not list_of_points[i][0] == list_of_points[j][0]:
#                 list_of_lines.append(calculate_line(list_of_points[i], list_of_points[j]))
#     return list_of_lines
#
#
# def make_lines_with_map(first_list, second_list):
#     list_of_points = list(map(make_pairs, first_list, second_list))
#     list_of_lines = get_lines(list_of_points)
#     print(list_of_lines)
#
#
# def make_lines_with_zip(first_list, second_list):
#     list_of_points = list(zip(first_list, second_list))
#     list_of_lines = get_lines(list_of_points)
#     print(list_of_lines)
#
#
# make_lines_with_map([1, 5, 2], [7, 9, 2])
# make_lines_with_zip([1, 5, 2], [7, 9, 2])

# Exercitiul 7

# def get_numbers(list_of_integers):
#     return list(zip(filter(lambda x: x % 2 == 0, list_of_integers), filter(lambda x: x % 2 == 1, list_of_integers)))
#
#
# print(get_numbers([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

# Exercitiul 8

# def sum_digits(x):
#     return sum(map(int, str(x)))
#
#
# def process(**kwargs):
#     list_of_fibonacci_items = [0, 1]
#     list_after_filter = []
#     list_after_limit = []
#     list_after_offset = []
#     a = 0
#     b = 1
#     while len(list_of_fibonacci_items) < 1000:
#         a, b = b, a + b
#         list_of_fibonacci_items.append(b)
#     if 'filters' in kwargs:
#         for i in list_of_fibonacci_items:
#             if kwargs.get('filters')[0](i) and kwargs.get('filters')[1](i):
#                 list_after_filter.append(i)
#     if 'offset' in kwargs:
#         for i in range(kwargs.get('offset'), len(list_after_filter)):
#             list_after_offset.append(list_after_filter[i])
#     if 'limit' in kwargs:
#         for i in range(0, kwargs.get('limit')):
#             list_after_limit.append(list_after_offset[i])
#     print(list_after_limit)
#
#
# process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2)

# Exercitiul 9

# def print_arguments(function):
#     def wrapper(*args, **kwargs):
#         print(args, kwargs)
#         return function(*args, **kwargs)
#     return wrapper
#
#
# @print_arguments
# def multiply_by_two(x):
#     return x * 2
#
#
# augmented_multiply_by_two = print_arguments(multiply_by_two)
# x = augmented_multiply_by_two(10)

dictionar ={(0, 1): 1}
if (0, 1) in dictionar:
    print(dictionar.get((0,1)))


























