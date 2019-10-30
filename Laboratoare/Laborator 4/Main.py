# Exercitiul 1
# def sort_tuples(list):
#     return sorted(list, key=lambda x: x[1])
#
#
# print(sort_tuples([("Miron", "Daniel"), ("Miron", "Andrei")]))

# Exercitiul 2
# def check_if_element_exists(list_tuples, string):
#     for i in list_tuples:
#         if i[1] == string:
#             return True
#     return False
#
#
# print(check_if_element_exists([("Miron", "Andrei"), ("Miron", "Daniel")], "Andrei"))

# Exercitiul 3
# dictionar = {
#
#     "+": lambda a, b: a + b,
#
#     "*": lambda a, b: a * b,
#
#     "/": lambda a, b: a / b,
#
#     "%": lambda a, b: a % b
#
#     }
#
#
# def apply_operator(operator, a, b):
#     print(dictionar[operator](a, b))
#
#
# apply_operator("*", 2, 3)

# Exercitiul 4
dictionar = {

    "print_all": lambda *a, **k: print(a, k),

    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),

    "print_only_args": lambda *a, **k: print(a),

    "print_only_kwargs": lambda *a, **k: print(k)

}


def apply_function(operator, *args, **kwargs):
    dictionar[operator](args, kwargs)


apply_function("print_only_args", 1, 3, nr=2)
