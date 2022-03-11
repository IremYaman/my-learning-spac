# x = 0
# while x <= 100:
#     if x % 2 == 1:
#         print(f"sayı tek: {x}")
#     else:
#         print(f"sayı çift: {x}")
#     x += 1

#####
    
# x = 0
# while x < 100:
#     x += 1
#     print(x)

#####

name = "" #False
while not name.strip():
    name = input("Adınız: ").capitalize()
print(f"Hoşgeldin, {name}")