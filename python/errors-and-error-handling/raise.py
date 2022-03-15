import re
def checkPassword(psw):
    if not len(psw) > 7:
        raise Exception("şifre en az 8 karakterden oluşmalı")
    elif not re.search( "[a-z]",psw):
        raise Exception("şifre küçük harf içermeli")
    elif not re.search( "[A-Z]",psw):
        raise Exception("şifre büyük harf içermeli")
    elif not re.search( "[_@$#]",psw):
        raise Exception("şifre alpha numeric karakter içermeli")
    elif re.search("/s",psw):
        raise Exception("şifre boşluk içermemeli")


password = "1234567aB_"

try:
    checkPassword(password)
except Exception as e:
    print(e)
else:
    print("geçerli parola")
finally:
    print("done")
