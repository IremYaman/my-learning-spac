import random

x = random.randint(1,101)
hak = 5 
while hak > 0:
    sayi = int(input("1-100 aralığında bir sayı giriniz: "))
    if sayi == x:
        print(f"Tebrikler, {5-hak}. defada sayıyı buldunuz! Aldığınız puan {hak*20}/100")
        break
    elif 101 > sayi > x:
        hak -= 1
        if hak > 0:
            print(f"AŞAĞI (kalan hakkınız: {hak})")
        else:
            print(f"Kalan hakkınız: 0. Sayıyı bulamadınız. Tutulan sayı: {x}. Aldığınız puan: 0/100")
    elif 0 < sayi < x:
        hak -= 1
        if hak > 0:
            print(f"YUKARI (kalan hakkınız: {hak})")
        else:
            print(f"Kalan hakkınız: 0. Sayıyı bulamadınız. Tutulan sayı: {x}. Aldığınız puan 0/100")
    else:
        print("1-100 aralığında bir sayı girmediniz.")