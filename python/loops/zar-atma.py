import random
from msvcrt import getch

while 1: 
    print("Zar atmak için Enter tuşuna, çıkış yapmak için Esc tuşuna basın.")
    key = ord(getch())
    if key == 13:
        print(random.randint(1,6))
    elif key == 27:
        print("Çıkış yaptınız. ")
        break
    else: 
        print("Yanlış tuşa bastınız.") 