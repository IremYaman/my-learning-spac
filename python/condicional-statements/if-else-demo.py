# name = input("Adınız: ")
# age = int(input("Yaşınız: "))
# education = input("Eğitim durumunuz: ").lower()

# if (age <= 18) and (education != "lise" or education == "üniversite"):
#     print(f"{name}, ehliyet alamazsın, yaşın 18'den küçük ve eğitim durumun yetersiz. ")
# else:
#     if age >= 18:
#         if education == "lise" or education == "üniversite":
#             print(f"{name}, ehliyet alabilirsin.")
#         else:
#             print(f"{name}, ehliyet alamazsın, eğitim durumun yetersiz.")
#     else:
#         print(f"{name}, ehliyet alamazsın, yaşın 18'den küçük.")

#####

# BirinciYazili = float(input("Birinci yazılı notunuz: "))
# IkınciYazili = float(input("İkinci yazılı notunuz: "))
# Sozlu = float(input("Sözlü notunuz: "))
# ortalama = (BirinciYazili + IkınciYazili + Sozlu) / 3

# if (ortalama >= 0) and (ortalama <= 24):
#     print(f"Ortalamanız {ortalama} olup 5 üzerinden notunuz: 0'dır.")
# elif (ortalama >= 25) and (ortalama <= 44):
#     print(f"Ortalamanız {ortalama} olup 5 üzerinden notunuz: 1'dir.")
# elif (ortalama >= 45) and (ortalama <= 54):
#     print(f"Ortalamanız {ortalama} olup 5 üzerinden notunuz: 2'dir.")
# elif (ortalama >= 55) and (ortalama <= 69):
#     print(f"Ortalamanız {ortalama} olup 5 üzerinden notunuz: 3'dür.")
# elif (ortalama >= 70) and (ortalama <= 84):
#     print(f"Ortalamanız {ortalama} olup 5 üzerinden notunuz: 4'dür.")
# elif (ortalama >= 85) and (ortalama <= 100):
#     print(f"Ortalamanız {ortalama} olup 5 üzerinden notunuz: 5'dir.")
# else:
#     print("Yanlış bilgi girdiniz.")

#####

# import datetime

# InputDate = input("Aracınız hangi tarihte trafiğe çıktı? (yıl/ay/gün): ")
# listDate = InputDate.split("/")
# today = datetime.datetime.today()
# date = datetime.datetime(int(listDate[0]), int(listDate[1]), int(listDate[2]))
# result = (today - date).days
# print(f"Aracınız {result} gündür trafikte.")

# if result <= 365:
#     print("1. Servis Aralığı")
# elif result > 365 and result <= 365*2:
#     print("2. Servis Aralığı")
# elif result > 365*2 and result <= 365*3:
#     print("3. Servis Aralığı")
# else:
#     print("Hatalı süre.") 