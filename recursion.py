def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
     return num * factorial(num - 1) # function calling intself called recursion


print(factorial(3))
print(factorial(4))

def fibo(n):
    if(n==0 or n==1):
        return 1
    else:
        return factorial(n-1)+factorial(n-2)

print(fibo(3))