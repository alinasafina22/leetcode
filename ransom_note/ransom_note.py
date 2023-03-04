from collections import Counter

'''
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using 
the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
'''


def canConstruct(ransomNote: str, magazine: str) -> bool:
    first_word = Counter(ransomNote)
    count = 0
    second_word = Counter(magazine)
    if first_word <= second_word:
        return True
    else:
        return False


