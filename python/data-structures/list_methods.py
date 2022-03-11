numbers = [ 1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)
val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]
numbers[4] = 40
numbers.append(49)                       # append en sona sayı eklemeyi sağlar
numbers.insert(3, 78)                    # insert istediğin konuma sayı eklemeyi sağlar
numbers.insert(-1, 52)
numbers.pop()                            # pop listeden eleman silmeyi sağlar, değer girilmezse sonuncu elemanı siler
numbers.remove(52)                       # remove girilen değeri bulup siler
numbers.sort()                           # sort liste elemanlarını küçükten büyüğe sıralar
letters.sort()
numbers.reverse()                        # reverse liste elemanlarını tersten yazar
letters.reverse()


# print(numbers)
# print(letters)

# print(len(numbers))
# print(len(letters))

# print(numbers.count(10))               # count belirtilen elemandan kaç adet olduğunu söyler
# print(letters.count("a"))

numbers.clear()
print(numbers)