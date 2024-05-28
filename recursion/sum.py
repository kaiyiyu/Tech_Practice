def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
    
print(sum_of_digits(12345)) # 15
print(sum_of_digits(123456789)) # 45