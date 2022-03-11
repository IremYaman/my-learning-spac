# firstnumber = int(input("Birinci sayıyı giriniz: "))
# secondnumber = int(input("İkinci sayıyı giriniz: "))
# result = firstnumber > secondnumber
# print(f"Birinci sayı ({firstnumber}) ikinci sayıdan ({secondnumber}) büyüktür. : {result}")

# vize1 = float(input("Birinci vize: "))
# vize2 = float(input("İkinci vize: "))
# final = float(input("Final: "))
# vizeOrt = ((vize1 + vize2) / 2) * (60/100)
# finalOrt = final * (40/100)
# result = vizeOrt + finalOrt
# print(f"not ortalamanız : {result} ve dersten geçme durumunuz: {result >= 50}")

# number = int(input("Bir sayı giriniz: "))
# tekcift = number % 2 == 0 
# print(f"Girdiğiniz sayının çift olma durumu: {tekcift}")

# number = int(input("Bir sayı giriniz: "))
# negatifpozitif = number > 0
# print(f"Girdiğiniz sayının pozitif olma durumu: {negatifpozitif} ")

mail = "email@sadikturan.com" 
parola = "abc123"

mailInput = str(input("Email giriniz: ").lower().strip())  # strip ve lower metodu
parolaInput = str(input("Parola giriniz: ").strip())
result1= mail == mailInput
result2 = parola == parolaInput
lastresult = result1 == result2
print(f"Girdiğiniz email adresi {result1}, girdiğiniz parola {result2}. Sonuç: {lastresult}")