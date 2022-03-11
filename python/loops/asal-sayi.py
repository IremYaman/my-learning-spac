
sayi = int(input("Bir sayı giriniz: "))
asalmi = True

if sayi == 1:
    asalmi = False
for x in range(2,sayi):
    if sayi % x == 0:
        asalmi = False
        break
if asalmi:
    print("sayı asaldır.")
else:
    print("sayı asal değildir.")