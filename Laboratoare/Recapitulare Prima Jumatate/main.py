import math


# Laborator 1

# Exercitiul 1


def gcd(a, b):
    while not b == 0:
        a, b = b, a % b
    return a


# Exercitiul 2

def get_vowels_number(text):
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    number = 0
    for i in text:
        if i.lower() in list_of_vowels:
            number += 1
    return number


# Exercitiul 3

def get_number_of_occurences(text1, text2):
    return text2.count(text1)


# Exercitiul 4

def modify_string(text):
    text_aux = ""
    for i in text:
        if i.isupper() and text.find(i) == 0:
            text_aux += i.lower()
        elif i.isupper():
            text_aux = text_aux + '_' + i.lower()
        else:
            text_aux += i
    return text_aux


# Laborator 2

# Exercitiul 1

def get_first_n_fibonnaci_numbers(n):
    list_of_numbers = [0, 1]
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        while len(list_of_numbers) < n:
            list_of_numbers.append(
                list_of_numbers[len(list_of_numbers) - 1] + list_of_numbers[len(list_of_numbers) - 2])
    return list_of_numbers


# Exercitiul 2

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_numbers_from_list(number_list):
    list_to_be_returned = []
    for i in number_list:
        if is_prime(i):
            list_to_be_returned.append(i)
    return sorted(list_to_be_returned)


# Exercitiul 3

def get_list_of_lines(list_of_points):
    list_to_be_returned = []
    for i in list_of_points:
        j = list_of_points.index(i) + 1
        while j < len(list_of_points):
            slope = (list_of_points[j][1] - i[1])
            list_to_be_returned.append((-slope, (list_of_points[j][0] - i[0]), slope * i[0] - slope * i[1]))
            j += 1
    return list_to_be_returned


# Rezolvarea pe o linie

list_of_points = [(1, 2), (2, 3), (4, 5)]  # Poate avea orice puncte
list_to_show = [
    (-(list_of_points[j][1] - i[1]), (list_of_points[j][0] - i[0]),
     (list_of_points[j][1] - i[1]) * i[0] - (list_of_points[j][1] - i[1]) * i[1])
    for i in list_of_points for j in range(list_of_points.index(i) + 1, len(list_of_points))]


# Exercitiul 4

def get_set_operations(first_list, second_list):
    first_list = set(first_list)
    second_list = set(second_list)
    return first_list & second_list, first_list | second_list, first_list - second_list, second_list - first_list


# Rezolvare cu lambda (de facut cast la set in lambda pentru a se putea face operatiile)
result = lambda first_list, second_list: (first_list & second_list, first_list | second_list,
                                          first_list - second_list, second_list - first_list)

# Exercitiul 5 DE IMPLEMENTAT

list_of_permutations = []


def get_combinations(list_of_numbers, k, first_element_pos):
    for i in range(1, len(list_of_numbers)):
        print("NOT IMPLEMENTED")


# Exercitiul 6

def get_elements(number, *args):
    dictionary = {}
    new_list = []
    for i in args:
        for j in i:
            if j not in dictionary:
                dictionary[j] = 1
            else:
                dictionary.update({j: dictionary.get(j) + 1})
    for i in dictionary.items():
        if i[1] == number:
            new_list.append(i[0])
    return new_list


# Exercitiul 7

def get_chars(flag, x=1, *args):
    final_list = []
    for i in args:
        aux_list = []
        for j in i:
            if flag is True and ord(j) % x == 0:
                aux_list.append(j)
            elif flag is False and ord(j) % x == 1:
                aux_list.append(j)
        final_list.append(aux_list)
    return final_list


# Exercitiul 8

def new_lists(*args):
    max_length = max([len(x) for x in args])
    for i in args:
        while len(i) < max_length:
            i.append(None)
    return list(zip(*args))


# Exercitiul 9

def sort_list(list_to_sort):
    return sorted(list_to_sort, key=lambda x: x[1][2])


# Laboratorul 3

# Exercitiul 1

def do_set_operations(first_list, second_list):
    first_list = set(first_list)
    second_list = set(second_list)
    final_set = set([])
    final_set.add(frozenset(first_list & second_list))
    final_set.add(frozenset(first_list | second_list))
    final_set.add(frozenset(first_list - second_list))
    final_set.add(frozenset(second_list - first_list))
    return final_set


# Exercitiul 2

def convert_string_dict(string):
    dictionary = {}
    for i in string:
        dictionary.update({i: string.count(i)})
    return dictionary


# Exercitiul 3

def parcuregere_recursiva_dict(dict1, dict2):
    print("Not Implemented")


# Exercitiul 4

def build_xml_element(tag, content, **kwargs):
    string = "<" + tag
    for i in kwargs.items():
        string += " " + i[0] + "=\\\"" + i[1] + "\\\""
    string += ">" + content + "<\\" + tag + ">"
    return string


# Exercitiul 5 Nu inteleg cerinta

# Exercitiul 6

def stupid_exercise(set_of_numbers):
    return len(set_of_numbers), 0


# Exercitiul 7

def add_operations_to_dict(dictionary, first_set, second_set):
    dictionary.update({str(first_set) + "|" + str(second_set): len(first_set | second_set)})
    dictionary.update({str(first_set) + "&" + str(second_set): len(first_set & second_set)})
    dictionary.update({str(first_set) + "-" + str(second_set): len(first_set - second_set)})
    dictionary.update({str(second_set) + "-" + str(first_set): len(second_set - first_set)})


def create_dictionary_with_set_operations(*args):
    dictionary = {}
    for i in range(0, len(args)):
        for j in range(i + 1, len(args)):
            add_operations_to_dict(dictionary, args[i], args[j])
    return dictionary


# Laboratorul 4

# Exercitiul 1

def sort_tuples(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])


# Exercitiul 2

def check_if_contained(list_of_tuples, string):
    return [True for i in list_of_tuples if i[1] == string][0]


# Exercitiul 3

operation_dic = {
    "+": lambda a, b: a + b,

    "*": lambda a, b: a * b,

    "/": lambda a, b: a / b,

    "%": lambda a, b: a % b
}


def apply_operator(operator, a, b):
    return operation_dic.get(operator)(a, b)


# Exercitiul 4

function_dict = {
    "print_all": lambda *a, **k: print(a, k),

    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),

    "print_only_args": lambda *a, **k: print(a),

    "print_only_kwargs": lambda *a, **k: print(k)
}


def apply_function(operator, *args, **kwargs):
    return function_dict.get(operator)(*args, **kwargs)


# Exercitiul 5

def make_new_dict(*args):
    new_dict = {}
    for i in args:
        for j in i.items():
            if j[0] in new_dict:
                new_dict.update({j[0]: [new_dict.get(j[0])]})
                new_dict.get(j[0]).append(j[1])
            else:
                new_dict.update({j[0]: j[1]})
    return new_dict


# Exercitiul 6

def recursive_dict(recursive_dictionary, given_separator='-', recursive_string=""):
    for k, v in recursive_dictionary.items():
        if isinstance(v, dict):
            recursive_dict(v, given_separator, recursive_string + k + given_separator)
        else:
            print(recursive_string, k, given_separator, v, sep="")


# Laboratorul 5

# Exercitiul 1
# Rezolvare facuta, e pe mai multe fisiere.

# Exercitiul 2

def return_sum(*args, **kwargs):
    suma = 0
    for i in kwargs.items():
        suma += i[1]
    return suma


print(return_sum(1, 2, c=3, d=4))
