# Exercitiul 1


# def operations(a, b):
#     a = frozenset(a)
#     b = frozenset(b)
#     c = [a.intersection(b), a.union(b), a.difference(b), b.difference(a)]
#     return set(c)
#
#
# print(operations([0, 1, 1, 5, 2, 3], [0, 1, 2, 6, 7]))

# Exercitiul 2


# def string_dictionary(string):
#     dictionary = {}
#     for i in string:
#         dictionary[i] = string.count(i)
#     print("{", end="")
#     for j in dictionary:
#         print("'" + j + "'" + ":" + dictionary[j].__str__(), end=";")
#     print("}", end="")
#
#
# string_dictionary("Ana has apples")

# Exercitiul 3


# def myprint(d):
#     for k, v in d.items():
#         if isinstance(v, dict):
#             myprint(v)
#         else:
#             print("{0} : {1}".format(k, v))
#
#
# myprint({u'xml': {u'config': {u'portstatus': {u'status': u'good'}, u'target': u'1'},
#                   u'port': u'11'}})

#Exercitiul 4


# def build_xml_element(tag, content, **dictionary):
#     xml = "<" + tag + " "
#     for i in dictionary:
#         xml = xml + i + "=\\" + dictionary[i] + "\\"
#     xml = xml + "id=\\\"someid\\\">" + content + "</" + tag + ">"
#     print(xml)
#
#
# build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ")

# Exercitiul 5
## DE TERMINAT

# def validate_dict(rules, dictionary):
#     print("ceva")
#
#
# validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out", "key3": "this is not valid"})

#Exercitiul 6


# def set_count(multime):
#     print((len(multime), 0))
#
#
# set_count({1,2,3})

#Exercitiul 7


def sets_to_dictionary(*sets):
    dictionary = {}
    lista = []
    for i in range(0, len(sets)):
        for j in range(i+1, len(sets)):
            lista.clear()
            for i1 in sets[i]:
                lista.append(i1)
            for i2 in sets[j]:
                lista.append(i2)
            dictionary.update({"{" + str(lista[0]) + "," + str(lista[1]) + "}" + "|" + "{" + str(lista[2]) + "," + str(lista[3]) + "}": len(sets[i].union(sets[j]))})
            dictionary.update({"{" + str(lista[0]) + "," + str(lista[1]) + "}" + "&" + "{" + str(lista[2]) + "," + str(lista[3]) + "}": len(sets[i].intersection(sets[j]))})
            dictionary.update({"{" + str(lista[0]) + "," + str(lista[1]) + "}" + "-" + "{" + str(lista[2]) + "," + str(lista[3]) + "}": len(sets[i].difference(sets[j]))})
            dictionary.update({"{" + str(lista[2]) + "," + str(lista[3]) + "}" + "-" + "{" + str(lista[0]) + "," + str(lista[1]) + "}": len(sets[j].difference(sets[i]))})
    count = 0
    for j in sets:
        count += 1
        if count == len(sets):
            print(j, end="")
        else:
            print(j, end=",")
    print("=>")
    print("{")
    for k in dictionary:
        print(k + ":" + str(dictionary[k]))
    print("}")


sets_to_dictionary({1, 2}, {2, 3}, {1, 5})
