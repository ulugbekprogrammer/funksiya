# a = 'John'
# b = 'Doe'

# def hello(a, b):
#     return f"Hello {a} {b}"

# # print(hello("John", "Doe"))

# res = hello(a, b)
# print(res)


# katta_son = lambda a, b: a if a > b else b

# natija = katta_son(10, 20)
# print(natija)


# def modul(x):
#     if x < 0:
#         return x * -1
#     return x

# ism = lambda a,: f'Good morning {a}'

# # def ism(a):
# #     return a
    
# res = ism('Ulugbek')
# print(res)


# age = lambda birth, cuurent_year: cuurent_year - birth

# current_year = int(input('Hozirgi yil: '))
# birth = int(input('Tug\'ilgan yil: '))

# res = age(birth, current_year)
# print(res)


# def salomBer(name):
#     print(f"Salom {name}")

# salomBer("Nodir")



# Uy ishi
# 1
# def PowerA3(a, b, c, d, e):
#     a_power = pow(a, 3)
#     b_power = pow(b, 3)
#     c_power = pow(c, 3)
#     d_power = pow(d, 3)
#     e_power = pow(e, 3)
#     return a_power, b_power, c_power, d_power, e_power

# a = float(input(('Son kiriting: ')))
# b = float(input(('Son kiriting: ')))
# c = float(input(('Son kiriting: ')))
# d = int(input(('Son kiriting: ')))
# e = int(input(('Son kiriting: ')))

# res = PowerA3(a, b, c, d, e)

# print(res)
# print(res[0])
# print(res[1])
# print(res[2])
# print(res[3])
# print(res[4])


# 2
# def PowerA3(a, b, c):
#     a_power = f'{a} ikkinchi darajasi ==> {a*2}, uchinchi darajasi ==> {a*3}, turtinchi darajasi ==> {a*4}'
#     b_power = f'{b} ikkinchi darajasi ==> {b*2}, uchinchi darajasi ==> {b*3}, turtinchi darajasi ==> {b*4}'
#     c_power = f'{c} ikkinchi darajasi ==> {c*2}, uchinchi darajasi ==> {c*3}, turtinchi darajasi ==> {c*4}'
#     return a_power, b_power, c_power
#
# a = float(input(('Son kiriting: ')))
# b = float(input(('Son kiriting: ')))
# c = float(input(('Son kiriting: ')))
#
#
# res = PowerA3(a, b, c)
# print(res[0])
# print(res[1])
# print(res[2])


# 3
# def Mean(a, b, c, d):
#     print((a+b)/2)
#     print((a+c)/2)
#     print((a+d)/2)

# a = float(input(('Son kiriting: ')))
# b = float(input(('Son kiriting: ')))
# c = float(input(('Son kiriting: ')))
# d = float(input(('Son kiriting: ')))

# Mean(a, b, c, d)


# 4
# def Triangle(a, b, c):
#     perimetr = a + b + c
#     s = perimetr / 2
#     yuza = (s*(s-a) * (s-b) * (s-c)) ** 0.5
#     return f'Perimetr: {perimetr}, Yuza: {yuza}'
    

# a = float(input(('Son kiriting: ')))
# b = float(input(('Son kiriting: ')))
# c = float(input(('Son kiriting: ')))

# res = Triangle(a, b, c)
# print(res)


# 6
# def DigitCountSum(a, b, c):
#     count = 0
#     summa = a + b + c 
#     if a > 0:
#         count += 1
#     if b > 0:
#         count += 1
#     if c > 0:
#         count += 1
#     else:
#         count = 0
#     return f"Summa: {summa}, Count: {count}"

# a = int(input('Son kiriting: '))
# b = int(input('Son kiriting: '))
# c = int(input('Son kiriting: '))

# res = DigitCountSum(a, b, c)
# print(res)


# 7
# def invertDigit(a):
#     teskari = 0
#     while a > 0:
#         oxirgi_raqam = a % 10
#         teskari = teskari * 10 + oxirgi_raqam
#         a = a // 10
    
#     return teskari

# a = int(input("Son kiriting: "))

# res = invertDigit(a)
# print(res)


# 8
# def AddRightDigit(a):
#     oxirgi_raqam = a % 10
#     if 1 <= oxirgi_raqam <= 9:
#         return True
#     return False

# a = int(input("Son kiriting: "))

# res = AddRightDigit(a)
# print(res)


# 9
# def AddLeftDigit(a):
#     while a >= 10:
#         n //= 10 
    
#     if 1 <= a <= 9:
#         return True
#     return False

# a = int(input("Son kiriting: "))

# res = AddLeftDigit(a)
# print(res)


# 10
# def Swap(a, b):
#     test = a
#     a = b
#     b = test
#     return a, b

# a = int(input("Son kiriting: "))    
# b = int(input("Son kiriting: "))

# res = Swap(a, b)
# print(res)


# 11
# def MinMax(a, b):
#     if a > b:
#         return a
#     return b

# a = int(input("Son kiriting: "))    
# b = int(input("Son kiriting: "))

# res = MinMax(a, b)
# print(res)


# 12
# def MinMax(a, b):
#     if a > b:
#         return a
#     return b

# a = int(input("Son kiriting: "))    
# b = int(input("Son kiriting: "))

# res = MinMax(a, b)
# print(res)


# 13
def MinMax(a, b):
    if a > b:
        return a
    return b

a = int(input("Son kiriting: "))    
b = int(input("Son kiriting: "))

res = MinMax(a, b)
print(res)



# def checknumberornot(a):
#     if a.isdigit():
#         return True
#     return False

# a = input("Son kiriting: ")

# res = checknumberornot(a)
# print(res)