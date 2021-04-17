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


sex = input("What is your sex? girl or boy?: ")
age = input("How old are you?: ")
age = int(age)

if sex == "girl" and age >= 18:
	print("Open the door")
elif sex == "girl" and age <= 18:
	print("Go away")
elif sex == "boy" and age >= 21:
	print("Open the door")
elif sex == "boy" and age <= 21:
	print("Go away")
else:
	print("You are not human")
