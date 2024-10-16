import functools
import time

@functools.lru_cache(maxsize= None)
def factorial(A):
    time.sleep(5)
    if (A == 0 or A == 1):
        return 1
    else:
        return A * factorial(A - 1)

print ("Factorial Of 5 : ",factorial(5))
print ("Factorial Of 7 : ",factorial(7))
print ("Factorial Of 9 : ",factorial(9))
print ("Factorial Of 3 : ",factorial(3))

print ("Factorial Of 5 : ",factorial(5))
print ("Factorial Of 7 : ",factorial(7))
print ("Factorial Of 9 : ",factorial(9))
print ("Factorial Of 3 : ",factorial(3))

print ("Factorial Of 4 : ",factorial(4))