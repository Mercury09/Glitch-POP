# #1---------------------------------------------------------------------------------------
# print('1', '2', '3', sep=' + ', end = ' ')
# print('=', 1 + 2 + 3, end = ' ')
# print('Ещё что?')

# print(1, 2, 3, 4, sep=' + ', end='')
# print(' = ', 1 + 2 + 3 + 4, sep='')

# print('2+3=', 23, 22, sep='+')

# a, b = 3, 4
# print(a,b)

# #2---------------------------------------------------------------------------------------
# print(11 + 6)
# print(11 - 6)
# print(11 * 6)
# print(11 // 6)
# print(11 ** 6)
# print(11 % 6)

# #Время 24:00---------------------------------------------------------------------------------------
# print((23 + 8)%24)
# print((7 - 8)%24)

# name = "Nazikow"
# age = 24

# print("Её зовут " + name + ". Eй уже " + str(age) + " годика. ", end = '')
# print("Бабуля уже =)")

# #3---------------------------------------------------------------------------------------
# print("abc " * 3)

# a = int(input())
# b = int(input())
# print(a + b)

# #Best_task
# a = int(input())
# num1 = a // 100
# num2 = (a // 10) % 10
# num3 = a % 10
# print(num1 + num2 + num3)
# print(str(num1) + " " + str(num2) + " " + str(num3) + " ")

# #4---------------------------------------------------------------------------------------
# n = int(input()) #Число
# k = int(input()) #Сколько убрать цифр справа
# print(n // 10**k)

# n = int(input())
# k = int(input())
# print((n + k - 1) // k) #Округление на большое число

# #Best_task---------------------------------------------------------------------------------------
# #Time 24 00
# a = int(input("Сколько минут?"))
# print("Hour: " + str((a // 60) % 24))
# print("Minute: " + str(a % 60))

# #Strange_test---------------------------------------------------------------------------------------
# #input 1 || 0, output 0 || 1
# a = int(input())
# print((a-1) // -1)

#God coding ---------------------------------------------------------------------------------------
a = int(input())
n = 1
m = 1
s = 1
d = 1
r = 1

while n <= a:
    print("   _~_    ", end ="")
    n += 1

print(" ")
while m <= a:
    print("  (o o)   ", end ="")
    m += 1

print(" ")
while s <= a:
    print(" /  V  \  ", end ="")
    s += 1

print(" ")
while d <= a:
    print("/(  _  )\ ", end ="")
    d += 1

print(" ")
while r <= a:
    print("  ^^ ^^   ", end ="")
    r += 1

# #-----------------------------------------------------------------------------------------------------------
#     H = int(input())
#     A = int(input())
#     B = int(input())
#     hab = 0
#     n = 0

#     while hab <= H:
#         hab += A
#         n += 1
#         while hab <= H:
#             hab = A - B
#     print(n)

# #############################################################################################
# start1 = int(input())
# start2 = int(input())
# finish1 = int(input())
# finish2 = int(input())

# is1startIn2 = start2 <= start1 <= finish2
# is1finishIn2 = start2 <= finish1 <= finish2
# is1in2 = is1startIn2 or is1finishIn2
# is2startIn1 = start1 <= start2 <= finish1
# is2finishIn1 = start1 <= finish2 <= finish1
# is2in1 = is2startIn1 or is2finishIn1
# answer = is1in2 or is2in1
# print(answer)

# #Best_task---------------------------------------------------------------------------------------
# #Chess
# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
# AisBlack = 0
# AisWhite = 0
# BisBlack = 0
# BisWhite = 0

# if a1 % 2 == 0 and a2 % 2 == 0 or a1 % 2 != 0 and a2 % 2 != 0:
#     AisBlack = 1
# elif a1 % 2 != 0 and a2 % 2 == 0 or a1 % 2 == 0 and a2 % 2 != 0:
#     AisWhite = 1

# if b1 % 2 == 0 and b2 % 2 == 0 or b1 % 2 != 0 and b2 % 2 != 0:
#     BisBlack = 1
# elif b1 % 2 != 0 and b2 % 2 == 0 or b1 % 2 == 0 and b2 % 2 != 0:
#     BisWhite = 1

# if AisBlack == 1 and BisBlack == 1:
#     print("YES")
# elif AisWhite == 1 and BisWhite == 1:
#     print("YES")
# else:
#     print("NO")

