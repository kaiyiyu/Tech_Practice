def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in permutation(s[:i] + s[i + 1:]):
                perms.append(c + perm)
        return perms
    
s1 = "abc"
print(permutation(s1)) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
                