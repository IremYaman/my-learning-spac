# def usalma(number):
#     def inner(power):
#         return number ** power
    
#     return inner

# two = usalma(2)
# print(two(3))


# def sayfaErisim(page):
#     def roleCheck(role):
#         if role == "Admin":
#             return "{0} rolü {1} sayfasına erişebilir.".format(role,page)

#     return roleCheck


# user1= sayfaErisim("index")
# print(user1("Admin"))


def islem(islemAdi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islemAdi == "toplama":
        return toplama
    else:
        return carpma


islem1 = islem("toplama")
print(islem1(2,3,4,5))

islem2 = islem("carpma")
print(islem2(2,3,4,5))
