# def change(n):
#     n[0] = "istanbul"


# sehirler = ["ankara", "izmir"]                 
# # change(sehirler)                             #direkt sehirler listesinde değişim yaptık
# n = sehirler[:]   #slicing                     #değişim n üzerinde oldu sehirler hala aynı
# change(n)
# print(n)
# print(sehirler)

# liste = []
# kacsayi = int(input("Kaç sayı toplamak istersiniz? "))
# while kacsayi > 0:
#     kacsayi -= 1
#     x = int(input("Sayı giriniz: "))
#     liste.append(x)

# def topla(list):
#     x = 0
#     for sayi in list:
#         x += sayi
#     return x

# print(topla(liste))




# def add(args):
#     return sum((args))

# liste = []
# kacsayi = int(input("Kaç sayı toplamak istersiniz? "))
# while kacsayi > 0:
#     kacsayi -= 1
#     x = int(input("Sayı giriniz: "))
#     liste.append(x)

# def convert(list):
#     return tuple(list)

# convert(liste)
# toplam = add(liste)
# print(f"Girdiğiniz sayıların toplamı: {toplam}")

def displayUser(**args):
    for key,value in args.items():
        print("{} is {}".format(key,value)) 


displayUser(name= "İrem", age= 19, city= "Ankara")
displayUser(name= "Mert", age= 21, city= "Kastamonu")


# * tuple
# ** dictionary 


