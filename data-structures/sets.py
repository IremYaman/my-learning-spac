fruits = { 'banana', 'apple', 'strawberry'}
# print(fruits[0]) XXX          # setler indekslenemez!

fruits.add('watermelon')        # add eleman ekleme
fruits.update(['mango', 'fig']) # update ile liste şeklinde eleman ekleme
# fruits.add('apple') XXX       # liste içerisinde bir elemandan sadece bir tane olabilir. apple'ı yeniden eklemeye çalıştığımızda ikinciye eklenmez
fruits.remove('mango')          # remove ve discard ile silme işlemi yapılabilir
fruits.discard('apple')  
fruits.pop()                    # pop rastgele bir eleman siler
fruits.clear()                  # clear tüm elemanları siler

for x in fruits:
    print(x)
print(fruits)

# myList = [1 ,2 ,4 ,2 ,1 ,7 ,5 ,4 ,5 ]
# print(set(myList))            # set ile listeler sete çevirilebilir


 