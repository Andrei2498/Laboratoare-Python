#Punctul 1

# import math
#
# list = [int(x) for x in input().split()]
# if(len(list)==1):
#     print(list[0])
# elif(len(list)==2):
#     print(math.gcd(list[0],list[1]))
# else:
#     a=list[0]
#     b=list[1]
#     cmmdc=math.gcd(a,b)
#     for i in range(2,len(list)):
#         cmmdc=math.gcd(cmmdc,list[i])
#     print(cmmdc)

#Punctul 2

# string=input()
# num_vowels=0
# for char in string:
#     if char in "aeiouAEIOU":
#         num_vowels=num_vowels+1
# print("Numar vocale: " , num_vowels)

#Punctul 3

# string=input()
# string=string.split()
# print(string[1].count(string[0]))

#Punctul 4

string = input()
new_string = ""
new_string += string[0].lower()
for i in range(1 , len(string)):
    if string[i].isupper():
        new_string += "_"
        new_string += string[i].lower()
    else:
        new_string += string[i].lower()
print(new_string)

#Punctul 5

# import numpy as np
#
# string="first_python_lab"
# input = np.loadtxt("Matrix", dtype='i', delimiter=',')
# n=len(input)*len(input)
# k=2
# poz1=len(input)-2
# poz2=0
# moves=0
# for i in range(0,len(input)):
#     print(string[input[0][i]-1],end="")
# for i in range(1,len(input)):
#     print(string[input[i][len(input)-1]-1],end="")
# for i in range(1,len(input)):
#     print(string[input[len(input)-1][len(input)-i-1]-1],end="")
#
# while k<len(input) :
#     if moves == 2:
#         k=k+1
#         moves=0
#     if moves == 0 and k%2 == 0:
#         for i in range(0,len(input)-k):
#             print(string[input[poz1-i][poz2]-1],end="")
#         poz1 = poz1-k+1
#     elif moves == 1 and k%2 == 0:
#         for i in range(1,len(input)-k+1):
#             print(string[input[poz1][poz2+i]-1],end="")
#         poz2 = poz2+k
#     elif moves == 0 and k%2 == 1:
#         for i in range(1,len(input)-k+1):
#             print(string[input[poz1+i][poz2]-1],end="")
#         poz1=poz1+len(input)-k
#     else:
#         for i in range(1,len(input)-k+1):
#             print(string[input[poz1][poz2-i]-1])
#         poz2=poz2-len(input)-k
#     moves = moves + 1

