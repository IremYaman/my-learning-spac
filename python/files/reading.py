# try:
#     file = open("newfile.txt","r",encoding="utf-8")  #"r" yazmaya gerek yok aslında
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()

# for döngüsü
file = open("newfile.txt","r",encoding="utf-8")
# for i in file:
#     print(i,end="")

# read() fonksiyonu
# print("içerik 1")
# content1 = file.read()
# print(content1)
# print("içerik 2")
# content2 = file.read()       #ikinciye yazmaz
# print(content2)

# content = file.read(5)        #içeriğin ilk 5 karakterini alır(5 byte=5 karakter)
# content = file.read(3)        #kaldığı yerden sonraki ilk 3 karakteri yazdırır
# print(content)

#*********readline() fonksiyonu
# print(file.readline(), end="")  #end="" eklemezsem sonuna boş bir satır koyuyor
# file.close()

#*********readlines() fonksiyonu
print(file.readlines())           #her satırı bir liste içinde toplar, her satır listenin bir elemanı olur
file.close()
