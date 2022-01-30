'''
  Hi, in these problem we will solve the problem about anagram using python.
  What is anagram may ask? 
  when two or more string have same character and same frequency  
'''

def key_count(str):
  key_str = {}

  for letter in str:
    if letter in key_str:
      key_str[letter] = key_str[letter] + 1
    else:
      key_str[letter] = 1

  return key_str

def is_anagram(str1,str2):
  key_str1 = {}
  key_str2 = {}

  key_str1 = key_count(str1)
  key_str2 = key_count(str2)

  for letter in str1:
    if letter in key_str2 and key_str1[letter] == key_str2[letter]:
      continue
    else:
      return False
  
  return True

str1 = "nameless"
str2 = "salesmen"

print(is_anagram(str1,str2))

'''
  In these video, he show another two way to solve instead of hash.
  In python a library is called collection in which a method called couter is does
  same as above
'''

from collections import Counter

print("using counter from collection lib")
print(Counter(str1) == Counter(str2)) 


'''
  another method is sorting the string and comparing. 
'''
print("using the sorted method")
print(sorted(str1) == sorted(str2))