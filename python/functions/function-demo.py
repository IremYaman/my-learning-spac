# kelime = input("Bir kelime giriniz: ")
# sayi = int(input("Bu kelimeyi kaç kez yazdırmak istiyorsunuz? "))

# def yazdir(word, num):
#     while num > 0:
#         num -= 1
#         print(word)
# yazdir(kelime, sayi)

# def yazdir(word,num):
#     print(word*num)

# def liste(params):
#     list= []
#     for param in params:                     #??? gereksiz
#         list.append(param)
#     return list 


# lis = []
# while True:
#     girilen = input("Parametre girmek için A harfini, listelemek için L harfini girin. ").capitalize()
#     if girilen == "A":
#         a = input("Parametre: ")
#         lis.append(a)
#     elif girilen == "L":
#         print(liste(lis))
#         break
#     else:
#         print("Hatalı tuşladın. Tekrar dene")

# num1 = int(input("Birinci sayı: "))
# num2 = int(input("İkinci sayı: "))
# def asalsayilar(num1,num2):
#     for sayi in range(num1, num2+1):
#         if sayi > 1:
#             for x in range(2, sayi):
#                 if sayi % x == 0: 
#                     break
#             else:
#                 print(sayi)



# asalsayilar(num1,num2)

sayi = int(input("Sayı: "))
def tambolen(sayi):
    tambolenler = []
    for x in range(1,sayi):
        if sayi % x == 0:
            tambolenler.append(x)

    print(tambolenler)

tambolen(sayi)



