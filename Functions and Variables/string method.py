#The Python string translate() method replaces each character in the string 
#using the given mapping table or dictionary.

s = 'abc12321cba'
print(s.translate({ord('b'): None}))

s1 = input("Enter a string s1: ")
s2 = input("Enter another string s2: ")
print(s1.translate({ord(i): None for i in s2}))