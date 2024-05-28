bin_1 = bin(64)
bin_2 = bin(7)

dec_1 = int(bin_1, 2)
dec_2 = int(bin_2, 2)

print(dec_1)
print(dec_2)

def binary_to_decimal(bin):
    decimal = 0
    str_bin = str(bin)
    exp = len((str_bin)) - 1
    
    for bit in str_bin:
        if bit == "1":
            decimal += 2 ** exp
        exp -= 1
        
    return decimal

print(binary_to_decimal(111))
print(binary_to_decimal(1001111))