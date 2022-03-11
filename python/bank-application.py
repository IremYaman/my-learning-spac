users = {
    'iremyaman': {
        'password': 'xyz111',
        'anahesap': 3000,
        'ekhesap': 2000
    },
    'mertkuzu': {
        'password': '123abc',
        'anahesap': 2000,
        'ekhesap': 1000

    }
}



def login():
    hak = 3
    while hak > 0:
        hak -= 1
        username = input("Kullanıcı adı: ").strip()
        password = input("Şifre: ").strip()
        if username in users:
            if users[username]['password'] == password:
                print("Giriş başarılı. ")
                return username
            else: 
                if hak > 0:
                    print("Hatalı giriş yaptınız. Yeniden deneyin. ")
                    user = None
                elif hak == 0:
                    print("Hatalı giriş yaptınız. Daha fazla deneyemezsiniz.")
                    user = None
        else:
            if hak > 0:
                print("Hatalı giriş yaptınız. Yeniden deneyin. ")
                user = None
            elif hak == 0:
                print("Kullanıcı adı hatalı. Daha fazla deneyemezsiniz.")
                user = None


def anamenu(a):
    print('''
        Lütfen yapmak istediğiniz işlemi seçin.
        [1]Bakiye sorgula
        [2]Para çek
        [3]Para yatır
        [q]Çıkış yap
        ''')
    x = input("Lütfen seçiminizi yapınız: ")
    if x == "1":
        bakiyesorgulama(a)
    elif x == "2":
        paracekme(a)
    elif x == "3":
        parayatirma(a)
    elif x == "q":
        print("Çıkış yaptınız.")
        main()
    else:
        print("Yanlış tuşlama yaptınız.")
        logout(a)


def bakiyesorgulama(a):
    print("Ana hesap bakiyeniz: " + str(users[a]['anahesap']))
    print("Ek hesap bakiyeniz: " + str(users[a]['ekhesap']))
    logout(a)


def paracekme(a):
    x = int(input("Çekmek istediğiniz tutarı girin: "))
    if x <= users[a]['anahesap']:
        print(f"İşlem başarılı. Paranızı alabilirsiniz. ")
        users[a]['anahesap'] -= x 
    elif x >= users[a]['anahesap']:
        y = input("Ana hesabınızın bakiyesi yetersiz. Ek hesabınızı da kullanarak denemek ister misiniz?(evet/hayır): ").lower()
        if y == "evet":
            if x <= users[a]['anahesap'] + users[a]['ekhesap']:
                print("İşlem başaralı. Paranızı alabilirsiniz. ")
                users[a]['ekhesap'] -= x - users[a]['anahesap']
                users[a]['anahesap'] = 0
                logout(a)
            elif x >= users[a]['anahesap'] + users[a]['ekhesap']:
                print("Bakiye yetersiz.")
                logout(a)
        elif y == "hayır":
            logout(a)
    else:
        print("İşlem başarısız. ")
        logout(a)


def parayatirma(a):
    hak = 3
    while hak > 0:
        hak -= 1
        print("[1] Ana hesap Bakiye: " + str(users[a]['anahesap']))
        print("[2] Ek hesap Bakiye: " + str(users[a]['ekhesap']))
        x = input("Para yatırmak istediğiniz hesabı seçin: ")
        y = int(input("Yatırmak istediğiniz miktarı girin: "))
        if x == "1":
            users[a]['anahesap'] += y
            print("İşlem başarılı. ")
            logout(a)
            break
        elif x == "2":
            users[a]['ekhesap'] += y
            print("İşlem başarılı. ")
            logout(a)
            break
        else:
            b = input("Yanlış tuşlama yaptınız. Yeniden deneyin veya çıkış yapın.(yeniden/çıkış): ").lower()
            if b == "yeniden":
                continue
            else:
                logout(a)
    

def logout(a):
    hak = 3
    while hak > 0:
        hak -=1
        girilen = input("Çıkış yapmak için X'i, ana menüye dönmek için A'yı tuşlayın: ").upper()
        if girilen == "X":
            print("Çıkış yaptınız.")
            main()
        elif girilen == "A":
            anamenu(a)
        else:
            print("Yanlış tuşlama yaptınız.")
            if hak == 0:
                print("Çıkış yapıldı.")
                main()
            

def main():
    global user
    print("Hoşgeldiniz, giriş yapmak için kullanıcı adınızı ve şifrenizi giriniz.")
    user = login()
    if user is not None:
        anamenu(user)


main()


