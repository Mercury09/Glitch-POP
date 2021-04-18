# def my_func(a,b):
# 	return a * b

# print(my_func(7,9))

def my_f(age):
	try:
		if int(age) >= 18:
			print("More than 18y")
		else:
			print("Less than 18y")
	except Exception as e:
		print(e,"Plese write number correct")
	
age = input("How old are you?:")
my_f(age)
