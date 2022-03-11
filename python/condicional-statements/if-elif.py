from traceback import print_tb


# x = int(input("x: "))
# y = int(input("y: "))

# if x > y:
#     print("x, y'den büyüktür. ")
# elif x == y:
#     print("x ve y eşittir. ")
# else:
#     print("y, x'den büyüktür.")

#####

number = float(input("Bir sayı giriniz: "))

if number > 0:
    print("Girdiğiniz sayı pozitiftir. ")
elif number == 0:
    print("Girdiğiniz sayı nötrdür. ")
else:
    print("Girdiğiniz sayı negatiftir. ")