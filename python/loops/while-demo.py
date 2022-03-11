# sayilar = [1,3,5,7,9,12,19,21]

# i = 0
# while i < (len(sayilar)):
#    print(sayilar[i])
#    i += 1

# firstNumber = int(input("Küçük sayıyı giriniz: "))
# secondNumber = int(input("Büyük sayıyı giriniz: "))
# while firstNumber < secondNumber:
#     firstNumber += 1
#     if firstNumber % 2 == 1:
#         print(f"tek sayı: {firstNumber}")

# i = 101
# while i > 1:
#     i -= 1
#     print(i)

# numbers = []

# i = 0
# while i < 5:
#     sayi = int(input("sayı: "))
#     numbers.append(sayi)
#     i += 1 
# numbers.sort()
# print(numbers)

urunSayisi = int(input("ürün sayısı giriniz: "))
urunler = []
i = 0
while i < urunSayisi:
    name = input("ürün adı: ")
    price= input("ürün fiyatı: ")
    urunler.append({
        "name" : name,
        "price" : price
    })
    i += 1
for urun in urunler:
    print(f'ürün adı: {urun["name"]}, ürün fiyatı: {urun["price"]}')



   