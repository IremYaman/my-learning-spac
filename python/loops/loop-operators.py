#range---

# for item in range(4,8):              # 4den 8e kadarki sayıları yazdırma
#     print(item)

# for number in range (50,100,10):     # 50den 100e kadarki sayıları onar onar yazdırma
#     print(number)

#enumerate---

# greeting = "hello"                   # enumerate harfleri tektek ayırıp index numaraları ile birlikte yazdırır
# for index,letter in enumerate(greeting):
#     print(f"index: {index}, letter: {letter}")

#zip---

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]           # zip farklı listelerden index numaraları aynı olan elemanları bir araya toplar
list3 = [100,200,300,400,500]

for item in zip(list1,list2,list3):
    print(item)
for a,b,c in zip(list1,list2,list3):
    print(a)