# Built-in
a = "4f"
b = "40"
c = "aa1"

dec_a = int(a, 16)
dec_b = int(b, 16)
dec_c = int(c, 16)

print(dec_a)
print(dec_b)
print(dec_c)

def hex_to_dec(hex):
    hexadecimal = hex.lower()
    decimal = 0
    power = len(hexadecimal) - 1
    
    for i in hexadecimal:
        if "0" <= i <= "9":
            decimal += int(i) * (16 ** power)
        elif "a" <= i <= "f":
            decimal += (ord(i) - ord("a") + 10) * (16 ** power)
            
        power -= 1
        
    return decimal

print(hex_to_dec(a))
print(hex_to_dec(b))
print(hex_to_dec(c))