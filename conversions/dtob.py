# Built in 
a = 79
b = 64
c = 7

binary_a = bin(a)[2:]
binary_b = bin(b)
binary_c = bin(c)

print(binary_a)
print(binary_b)
print(binary_c)

# Custom implementation
def decimal_to_binary(decimal):
    if decimal >= 1:
        quotient = decimal // 2
        decimal_to_binary(quotient)
    print(decimal % 2, end="" )
    
decimal_to_binary(a)
print()
decimal_to_binary(b)
print()
decimal_to_binary(c)
print()    


print(5 // 2)
print(5 % 2)