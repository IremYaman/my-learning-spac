message = "Hello there. My name is İrem Yaman"
                                              # parantez içine bir şey yazılmazsa:
# message = message.upper()                   # upper tüm harfleri büyük harfe çevirir.
# message = message.lower()                   # lower tüm harfleri küçük harfe çevirir.
# message = message.title()                   # title her kelimenin baş harfini büyüğe çevirir.
# message = message.capitalize()              # capitalize yalnızca girilen yazının ilk harfini büyüğe çevirir.
# message = message.strip()                   # strip girilen yazının başındaki ve sonundaki boşlukları siler.
# message = message.split()                   # split girilen yazıyı kelimelerine ayırır.

    # message = message.split(".")
    # print(message)  
    # print(message[1])            
       
# message = "***".join(message)               # join ayrılmış olan yazıları birleştirir.
# print(message)

# index = message.find("İrem")                # find arattığımız kelimenin hangi karakterden itibaren başladığını söyler.
# print(index)                                 (değer pozitif çıkarsa kelime var, -1 çıkarsa yok)
# print(message[25:29])

# isFound = message.startswith("H")           # startswith metnin ilk harfinin aradığımız harf olup olamadığını tespit eder.   
# print(isFound)                              # bool ile sonuç alınır (sanırım?)
                                              # büyük harf küçük harf duyarlılığı vardır.

# isTrue = message.endswith("n")              # endswith metnin son harfinin aradığımız harf olup olmadığını tespit eder. 
# print(isTrue)

# message = message.replace("İrem", "Mert")   # replace metin içerisinde karakter değişimi yapmamızı sağlar.
#                  .replace("Yaman", "Kuzu") 
# print(message)                              

# message = message.center(100)               # center metnin başına ve sonuna girdiğimiz değer kadar boşluk bırakır.
# print(message)
# message = message.center(100, "*") 
# print(message)

# result = "Hello".isalpha                    # isalpha metnin alfabetik olup olmadığını söyler
# print(result)

# result = "123".isdigit                      # isdigit metnin sayısal olup olmadığını söyler
# print(result)

# result = "contents".ljust(50, "*")          # ljust metni sola yaslayıp belirtilen birim kadar, belirtilen ifadeden sağa ekler
# result = "contents".rjust(50, "*")          # rjust metni sağa yaslayıp belirtilen birim kadar, belirtilen ifadeden sola ekler
# print(result)

