'''
Created on 24. 8. 2026

@author: valic
'''

def remove_duplicities(s):
    l = len(s)
    i = 0
    while l - i - 1 > 0:
        if s[i] == s[i + 1]:
            s = s.replace(s[i], "")
            l = len(s)
        i += 1
    return s

def has_duplicities(s):
    l = len(s)
    i = 0
    while l - i - 1 > 0:
        if s[i] == s[i + 1]:
            return True
        i += 1
    return False

def alternate2(s):
    lengths = []
    text = s
    s = remove_duplicities(s)
    for i in range(len(text)):
        while len(set(s)) != 2 :
            if has_duplicities(s):
                s = remove_duplicities(s)
            s = s.replace(s[i], "")
        lengths.append(len(s))
    print(lengths)
    
    return max(lengths)

def has_adjacent_duplicates(s):
    return any(c1 == c2 for c1, c2 in zip(s, s[1:]))

def alternate(s):
    lengths = [0]
    unique_char = list(set(s))
    for i in range(len(unique_char)):
        for j in range(len(unique_char)):
            if unique_char[i] == unique_char[j]:
                continue
            keep = {unique_char[i], unique_char[j]}  
            alter = ''.join(x for x in s if x in keep)
            if not has_adjacent_duplicates(alter):
                lengths.append(len(alter))
    
    return max(lengths)

if __name__ == '__main__':
# abaacdabd        beabeefeab
    s = input()

    result = alternate(s)
    
    print(result)