# def total(num1, num2):
#     return num1 + num2


# a = total(2019,277)
# print(a)

isim = input("Adınız: ").capitalize()
dogumyili = int(input("Doğum yılınız: "))

def yashesaplama(dogumyili):
    return 2022 - dogumyili


def emekliligekalan(dogumyili, isim):
    # '''
    # DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi   #Fonksiyon bilgisi ekleme
    # INPUT: Dogum yili, isim
    # OUTPUT: Hesaplanan yil bilgisi
    # '''
    yas = yashesaplama(dogumyili)
    emeklilik = 65
    kalan = emeklilik - yas

    if kalan > 0:
        print(f"{isim}, emekliliğine {kalan} yıl kaldı.")
    else:
        print(f"{isim}, zaten emeklisin.")

emekliligekalan(dogumyili,isim)