# liste = ["1","3","8","10a","b9","abc","50"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

###########


# while True:
#     print("çıkış yapmak için q tuşlayabilirsiniz")
#     x = input("x: ")
#     if x == "q":
#         break

#     try:
#         result = int(x)
#         print("başarılı")
#     except ValueError:
#         print("başarısız (sayı girmelisiniz)")

###########

# import re 

# def setPassword(psw):
#     if re.search("[çşğüöıİ]", psw):
#         raise Exception ("şifre türkçe karakter içermemeli")
#     else:
#         print("geçerli parola")
        

# password = input("parola giriniz: ")

# setPassword(password)

#############

def faktoriyel(x):
    x = int(x) 
    if x < 0:
        raise ValueError("negatif sayı")

    result = 1
    for i in range(1, x):
        result *= i

    return result


x = input("faktöriyeli bulunacak sayıyı girin: ")
print(faktoriyel(x))

        









