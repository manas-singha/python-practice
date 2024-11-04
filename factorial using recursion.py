def factorial(n):
    if (n==0):#Base case :where we do not call any function
        return 1
    return n * factorial(n-1)
print(factorial(5))