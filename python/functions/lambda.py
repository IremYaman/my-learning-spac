def square(num): return num**2
numbers = [1,2,3,4]
result =list(map(square, numbers))                #map methodu 
print(result)

numbers = [1,2,3,4]
result = list(map(lambda num: num**2, numbers))   #lambda1
print(result)

square = lambda num: num**2
numbers = [1,2,3,4]
result = list(map(square, numbers))               #lambda2
print(result)

num = [1,2,3,4]
cift = lambda num: num%2 == 0

result = cift(num[2])
print(result)
