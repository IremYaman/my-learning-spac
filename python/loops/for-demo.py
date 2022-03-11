# sayilar = [1,3,5,7,9,12,19,21]
# for num in sayilar:
#     if num % 3 == 0:
#         print(num)
# toplam = 0
# for num in sayilar:
#     toplam += num
# print("toplam:", toplam)

# for num in sayilar:
#     if (num % 2 == 1):
#         print(num ** 2)

#####

# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
# for s in sehirler:
#     if len(s) >= 5:
#         print(s)

#####



urunler = [
    {"name" : "samsung s6", "price" : "3000"},
    {"name" : "samsung s7", "price" : "4000"},
    {"name" : "samsung s8", "price" : "5000"},
    {"name" : "samsung s9", "price" : "6000"},
    {"name" : "samsung s10", "price" : "7000"}

]

toplam = 0
for products in urunler:
    fiyat = int(products["price"])
#     toplam += fiyat
# print(toplam)
    if fiyat <= 5000:
        print(products["name"])

    
        

