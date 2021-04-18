 #Hello World

 #-*- coding: utf-8 -*-
# # print("Salem Alem")
# print("Glitch-POP")
# '''
# sdasdas

# '''
# print("Ulpan Chert")

#date types


# data types

# string
# a = 'asdasd'
# b = "asdasdasd"
# c = '''asdasdasd'''

# int
# a = 1123

# # float
# a = 23.123

# a1 = [1,2,3, '223']

# d = {
#   'asd': 123,
#   '23': 233
# }

# # boolean
# a = True
# a = False


# a = '123'
# a = str(a)
# print(a)
# print(type(a))

# a = 1
# a = str(a)

# print(bool(a))

# a = range(5)
# print(a)

# a = 1
# b = '1'
# c = 1.14

# a = float(a)
# b = float(b)
# c = float(c)
# d = a + b + c

# print(round(d,2))
# Bla-bl-bla
# asd ad =asd

# a = input("Write First number\n")
# b = input("Write Second number\n")
# c = input("Write Third number\n")

# w = int(a) * int(b) * int(c)
# print(w)

# t = input("write radius\n")
# S = 3.14 * int(t)**2
# print(S)

# name = input("Write name")
# a = f"Hello {name}"
# print(a)

# a = "Hello Banana greps apple Banana banana"
# x = a.replace("Banana", "BANANA")
# f = x.replace("banana", "BANANA")
# print(f)
# t = f.replace("BANANA", "apple")
# print(t)

# password1 = '2222'#Jack
# password2 = '3333'#Nick

# user_input = input("Введи пароль")

# if user_input == password1:
#   print('Hello Jack')
# elif user_input == password2:
#   print('hello Nick')
# else:
#   print('wrong password!')

# a = input("Write first number\n")
# c = input("Choose one of operation: +, -, *, /\n")
# b = input("Write second number\n")

# a = int(a)
# b = int(b)

# if c == "+":
# 	w = a + b
# 	print(w)
# 	print(w)
# elif c == "*":
# 	w = a * b
# 	print(w)
# elif c == "/":
# 	if b == 0:
# 		print("Somthing wrong, b != 0")
# 	else:
# 		w = a / b
# 		print(w)
# else:
# 	print("nice")


# sex = input("What is your sex? girl or boy?: ")
# age = input("How old are you?: ")
# age = float(age)
# sex = sex.lower()

# if sex == "girl" and age >= 18:
# 	print("Open the door")
# elif sex == "girl" and age <= 18:
# 	print("Go away")
# elif sex == "boy" and age >= 21:
# 	print("Open the door")
# elif sex == "boy" and age <= 21:
# 	print("Go away")
# else:
# 	print("You are not human")


# d = {
#   'name' : 'Egor',
#   'surname': 'EgorUlyKotiBar',
#   'pas': 123123,
#   'WW': True,
#   'array': [12,2,3,24,3],
#   'dd': {
#     '2level': 'Egor2',
#     '2pas': 21312
#   }
# }

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
# # ['apple', 'banana', 'cherry', 'orange']

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[4:])
# # ["kiwi", "melon", "mango"]

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[2] = 'KKKKK'
# fruit = thislist[3]
# print(thislist)
# print(fruit)

# a = input("Write a = ")
# b = input("Write b = ")
# a = int(a)
# b = int(b)

# a = a + b
# b = a - b
# a = a - b

# print("a= " + str(a) + " b= " + str(b) + " ")


# StrList = ["cherry","range","red","panda","cat","toyota","apple"]
# IntList = [5,7,4,9,2,3,1,8]

# StrList.sort()
# IntList.sort()
# print(StrList)
# print(IntList)

# for i in StrList:
# 	print(i)
	
List = "asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA"
List2 = List
List2 = List2.upper()
List = List.split(' ')
List2 = List2.split(' ')
for i in range(0,len(List2)):
	if List2[i] == "BANANA":
		List[i] = "BANANA"
List = ' '.join(List)
print(List)


