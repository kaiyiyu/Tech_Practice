# Built-in
# Built in 
a = 79
b = 64
c = 7

hex_a = hex(a)[2:]
hex_b = hex(b)[2:]
hex_c = hex(c)[2:]

print(hex_a)
print(hex_b)
print(hex_c)

def dec_to_hex(decimal):
    hex_chars = "0123456789ABCDEF"
    hex = ""
    
    while decimal > 0:
        remainder = decimal % 16
        hex = hex_chars[remainder] + hex
        decimal = decimal // 16
    
    return hex

print(dec_to_hex(a))
print(dec_to_hex(b))
print(dec_to_hex(c))