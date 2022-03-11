username = "iremyaman"
password = "abc123"

IsUsername = input("Kullanıcı adınızı giriniz: ")
IsPassword = input("Şifrenizi giriniz: ")


if username == IsUsername:
    if password == IsPassword:
            print(f"Hoşgeldin, {username}. ")
    else:
            print("Şifre hatalı. ")
elif username != IsUsername:
    if password == IsPassword:
            print(f"Kullanıcı adı hatalı.")
    else:
            print("Kullanıcı adı ve şifre hatalı. ")


        


        