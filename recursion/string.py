def string_reversal(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + string_reversal(s[:-1])
    
s1 = "hello"
print(string_reversal(s1)) # olleh