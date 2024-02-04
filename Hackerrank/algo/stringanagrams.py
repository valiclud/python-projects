'''
Created on 2. 8. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys
from itertools import permutations

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    anagrams = []
    count = 0
    thisdict = {}
    #getting all permutations
    index = 0
    
    chars = list(s.strip())
    
    for ch in chars:
        sorted_chars = sorted(chars[:index])
        #chunks = [chars[i:i+index] for i in range(1, len(chars), index)]
        for i in range(0, len(chars)):
            c = sorted(chars[:i])
            if (c == sorted_chars and len(c) != 1):
                anagrams.append(''.join(c))
                key = ''.join(c)
                if key in thisdict:
                    value = thisdict.get(key)
                    value.append(i)
                    thisdict[key] = value
                else :
                    thisdict[key] = [i]
        index +=1
    print(anagrams)
    print(thisdict)
    #treating single character        
    for index , ch in enumerate(list(s)):
        if s.count(ch)>=2:
            anagrams.append(ch)
            res = [i for i in range(0, len(s)) if s.startswith(ch, i)]
            if (len(res) == 0 or res == [0]):
                continue
            thisdict[ch] = res
    print(thisdict)   
    
    #thisdict = {key:val for key, val in thisdict.items() if val != [0]} 
       
    print(thisdict)
    #filling dictionary        
        
    return count


def sherlockAndAnagrams2(s):
    anagrams = []
    count = 0
    thisdict = {}
    #getting all permutations
    index = 1
    
    chars = list(s.strip())
    
    for ch in chars:
        print(chars[:index])
        if (index > len(s)//2 + 1):
            break
        if (len(set(chars[:index]).intersection(set(chars))) > 1):
            for p in lexico_permute_string(chars[:index]):
                if s.count(p)==0:
                    continue
                anagrams.append(p)
        index +=1
    
    #for chj in range(len(s.strip())):
    #    if (index > len(s)//2 + 1):
    #        break
    #    for p in lexico_permute_string(s[:index]):
    #        if s.count(p)==0:
    #            continue
    #        anagrams.append(p)
    #    index +=1
    print(anagrams)
    #treating single character        
    for index , ch in enumerate(list(s)):
        if s.count(ch)>=2:
            anagrams.append(ch)
    #filling dictionary        
    for index, value in enumerate(anagrams):
        res = [i for i in range(0, len(s)) if s.startswith(value, i)]
        if (len(res) == 0 or res == [0]):
            continue
        thisdict[value] = res
        
    # final counting
    for name, l in thisdict.items():
        if (len(l) == 1):
            count +=1
        elif (len(l) == 2):
            if len(name) == 1:
                count +=1
            else :
                count +=2
        else:
            fakt = mathematics.factorial(len(l) - 1)
            count += fakt
    return count


def lexico_permute_string(s):
    ''' Generate all permutations in lexicographic order of string `s`

        This algorithm, due to Narayana Pandita, is from
        https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

        To produce the next permutation in lexicographic order of sequence `a`

        1. Find the largest index j such that a[j] < a[j + 1]. If no such index exists, 
        the permutation is the last permutation.
        2. Find the largest index k greater than j such that a[j] < a[k].
        3. Swap the value of a[j] with that of a[k].
        4. Reverse the sequence from a[j + 1] up to and including the final element a[n].
    '''

    #a = sorted(s)
    a = list(s)
    n = len(a) - 1
    while True:
        yield ''.join(a)

        #1. Find the largest index j such that a[j] < a[j + 1]
        for j in range(n-1, -1, -1):
            if a[j] < a[j + 1]:
                break
        else:
            return

        #2. Find the largest index k greater than j such that a[j] < a[k]
        v = a[j]
        for k in range(n, j, -1):
            if v < a[k]:
                break

        #3. Swap the value of a[j] with that of a[k].
        a[j], a[k] = a[k], a[j]

        #4. Reverse the tail of the sequence
        a[j+1:] = a[j+1:][::-1]




def sherlockAndAnagrams1(s):
    anagrams = []
    count = 0
    thisdict = {}
    #getting all permutations
    index = 1
    for chj in range(len(s.strip())):
        if (index >= len(s)):
            break
        for p in list(permutations(s[:index])):
            if s.count(''.join(p))>0:
                anagrams.append(''.join(p))
        index +=1
    #treating single character        
    for index , ch in enumerate(list(s)):
        if s.count(ch)>=2:
            anagrams.append(ch)
    #removing duplicates 
    #anagrams = list(dict.fromkeys(anagrams))
    #filling dictionary        
    for index, value in enumerate(anagrams):
        res = [i for i in range(0, len(s)) if s.startswith(value, i)]
        if (len(res) == 0 or res == [0]):
            continue
        thisdict[value] = res
        
    # final counting
    for name, l in thisdict.items():
        if (len(l) == 1):
            count +=1
        elif (len(l) == 2):
            if len(name) == 1:
                count +=1
            else :
                count +=2
        else:
            fakt = mathematics.factorial(len(l) - 1)
            count += fakt
    return count
    
    #removing inversed substring
    #for a in anagrams:
    #    if a[::-1] in anagrams:
    #        anagrams.remove(a)
    
    print(count)
    print(anagrams)
    print(thisdict)
    thisdict.pop(str([0]))
    print(thisdict)
    return len(thisdict)
       
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)

    #    fptr.write(str(result) + '\n')

    #fptr.close()
