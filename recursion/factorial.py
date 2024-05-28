def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) # 120
print(factorial(10)) # 3628800
print(factorial(0)) # 1