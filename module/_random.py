import random

result = random.random()                 #0-1
result = random.uniform(10,100)          #girilen aralıkta float sayı verir
result = random.randint(10,100)          #girilen aralıkta integer sayı verir

greeting = "hello there"
names = ["ali","ayşe","ahmet","merve"]
result = random.choice(names)           #listeden random elemen verir (choices yazarsan liste içinde oluyor)
result = random.choice(greeting)        #stringlerde yazılan her bir harf veya ifade bir elemandır

liste = list(range(10))
random.shuffle(liste)                   #liste elemanlarını karıştırıp yazdırdık
result = liste

liste  = range(100)
result = random.sample(liste,3)         #belirtilen listeden random 3 eleman yazdırır
result = random.sample(names,2)

print(result)