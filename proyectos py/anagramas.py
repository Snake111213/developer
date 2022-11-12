'''
c1 = Counter(str1)
c2 = Counter(str2)
print(c1)
print(c2)
c1 == c2
True
from collections import Counter
str1 = 'sav4e'
str2 = 'vase'

def are_anagrams(word1,word2):
    if Counter(word1) == Counter(word2):
        return True
    else:
        return False
    
are_anagrams(str1, str2)
True
print(are_anagrams)'''

from collections import Counter

def are_anagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
    
    are_anagrams('below','elbow')
    True
    are_anagrams('state','tasted')
    False
    
    print(are_anagrams)