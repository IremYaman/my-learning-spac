# ogrenciler = {}
# number = input('öğrenci no: ') 
# name = input('öğrenci adı: ')
# surname = input('öğrenci soyadı: ')
# phone = input('öğrenci telefonı: ')

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }
                                    #iki metod da kullanılabilir

# ogrenciler.update({
#     number: {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone

#     }
# })

ogrenciler = {}
number = input('öğrenci no: ') 
name = input('öğrenci adı: ')
surname = input('öğrenci soyadı: ')
phone = input('öğrenci telefonı: ')

ogrenciler.update({
    number: {
    'ad': name,
    'soyad': surname,
    'telefon': phone

    }
})

number = input('öğrenci no: ') 
name = input('öğrenci adı: ')
surname = input('öğrenci soyadı: ')
phone = input('öğrenci telefonı: ')

ogrenciler.update({
    number: {
    'ad': name,
    'soyad': surname,
    'telefon': phone

    }
})

number = input('öğrenci no: ') 
name = input('öğrenci adı: ')
surname = input('öğrenci soyadı: ')
phone = input('öğrenci telefonı: ')

ogrenciler.update({
    number: {
    'ad': name,
    'soyad': surname,
    'telefon': phone

    }
})

print(ogrenciler)

print('*'*50)

OgrNo = input('öğrenci no: ')
ogrenci = ogrenciler[OgrNo]
print(ogrenci)

print(f"Aradığınız {OgrNo} nolu öğrencinin adı: {ogrenci['ad']}, soyadı: {ogrenci['soyad']} ve telefon numarası: {ogrenci['telefon']}'dır.")