# girilenSayi = int(input("Bir sayı giriniz: "))
# if girilenSayi >= 0 and girilenSayi <= 100:
#     print("Girdiğiniz sayı 0 ile 100 arasında. ")
# else:
#     print("Girdiğiniz sayı 0 ile 100 arasında değil. ")

#####

# girilenSayi = int(input("Bir sayı giriniz: "))

# if girilenSayi % 2 != 0 and girilenSayi <= 0:
#     print("Girdiğiniz sayı çift veya pozitif değildir. ")
# else: 
#     if girilenSayi > 0:
#         if girilenSayi % 2 == 0:
#             print("Girdiğiniz sayı çift ve pozitiftir.")
#         else:
#             print("Girdiğiniz sayı pozitif fakat çift değildir. ")
#     else:
#         print("Girdiğiniz sayı çift fakat pozitif değildir. ")

#####

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a > b and a > c:
#     if b > c:
#         print("a>b>c")
#     elif b == c:
#         print("a>b=c")
#     else:
#         print("a>c>b")
# elif b > a and b > c:
#     if a > c:
#         print("b>a>c")
#     elif a == c:
#         print("b>a=c")
#     else: 
#         print("b>c>a")
# elif c > a and c > b:
#     if a > b:
#         print("c>a>b")
#     elif a == b:
#         print("c>a=b")
#     else:
#         print("c>b>a")
# elif a == b and a > c:
#     print("a=b>c")
# elif b == c and b > a:
#     print("b=c>a")
# elif a == c and a > b:
#     print("a=c>b")
# else:
#     print("a=b=c")

#####

# name = input("Adınız: ").capitalize()
# height = float(input("Boyunuz: "))
# weight = float(input("Kilonuz: "))

# KiloIndeksi = weight / (height ** 2)

# if KiloIndeksi >= 0 and KiloIndeksi <= 18.4:
#     print(f"{name}, kilo indeksin {KiloIndeksi} ve zayıfsın.")
# elif KiloIndeksi >= 18.5 and KiloIndeksi <= 24.9:
#     print(f"{name}, kilo indeksin {KiloIndeksi} ve normalsin.")
# elif KiloIndeksi >= 25.0 and KiloIndeksi <= 29.9:
#     print(f"{name}, kilo indeksin {KiloIndeksi} ve fazla kilolusun.")
# elif KiloIndeksi >= 30:
#     print(f"{name}, kilo indeksin {KiloIndeksi} ve obezsin.")
# else: 
#     print("Yanlış değer girdiniz.")

#####

# vize1 = float(input("Birinci vize notunuzu giriniz: "))
# vize2 = float(input("İkinci vize notunuzu giriniz: "))
# final = float(input("Final notunuzu giriniz: "))

# ort = ((vize1 + vize2) / 2) * 0.6 + final * 0.4

# if ort >= 50:
#     if final >= 50:
#         print(f"Ortalamanız {ort} ve final notunuz {final}, dersi geçtiniz. ")
#     else:
#         print(f"Ortalamanız {ort} fakat final notunuz {final}, dersten kaldınız. ")
# elif final >= 70:
#     print(f"Ortalamanız {ort} fakat final notunuz {final}, dersi geçtiniz. ")
# else:
#     print(f"Ortalamanız {ort} ve final notunuz {final}, dersten kaldınız. ")



