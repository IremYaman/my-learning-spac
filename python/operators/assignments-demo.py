x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# a= int(input("Birinci sayı: "))
# b= int(input("İkinci sayı: "))

# print(a*b-(x+y+z))

# result = y // x

# toplam = (x + y + z)
# result = toplam % 3

# result = y ** x

# x, *y, z = numbers
# result = z ** 3

x, *y, z = numbers
result = y[0] + y[1] + y[2]
print(result)