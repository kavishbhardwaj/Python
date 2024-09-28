s = input()
l = len(s)
flag = True
for i in range(0,l-1):
    if s[i] != s[l-i-1]:
        flag = False
if flag:
    print("PALINDROME")
else: 
    print("NOT PALINDROME")   