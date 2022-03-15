# YÖNTEM 1
# import math
# import math as islem            #math modülünü başka bir ad ile kullandık

# # value = dir(math)             #modülün tüm fonksiyonlarını gösterir
# # value = help(math)            #modülü açıklar ve modülün tüm fonksiyonlarını tek tek açıklar
# # value = help(math.factorial)  #belli bir fonksiyonun kullanımını görmek için
# # value = math.sqrt(49)         #karekökü 49 olan sayıyı yazdırır
# # value = math.factorial(5)     #faktöriyel hesaplama
# # value = math.floor(5.9)       #aşağı doğru yuvarlama yapar
# # value = math.ceil(5.1)        #yukarı doğru yuvarlama yapar
# value = islem.factorial(3)

# print(value)


# YÖNTEM 2
# from math import *              #* tüm fonksiyonları import etmemizi sağlar

# def sqrt(x):
#     print("x:" + str(x))        #fonksiyon bu konumdayken modülün fonksiyonu kullanılır


from math import factorial,sqrt

def sqrt(x):                      #fonksiyon bu konumdayken modülün fonksiyonu kullanılmaz. cevap olarak tanımladığımız fonksiyonu alırız
    print("x:" + str(x))

# value = factorial(4)            #bu yöntem fonksiyonları modül adı yazmadan kullanabilememizi sağlar
value = sqrt(6)

print(value)

