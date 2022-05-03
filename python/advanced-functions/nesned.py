# def outer(num1):
#     def inner(num1):
#         return num1 + 1
#     print(num1 * inner(num1))

# outer(5)
# inner(5)   #outer içine tanımlanmış bir fonksiyon olduğu için ayrı kullanılamaz.

from unittest import expectedFailure


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >= 0:
        raise ValueError("number must be bigger than or iqual to 0")

    def inner_function(number):
        if number <= 1:
            return 1
    
        return number * inner_function(number-1)
    return inner_function(number)

try:
    print(factorial(5))
except Exception as ex:
    print(ex)
