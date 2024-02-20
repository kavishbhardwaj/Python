from math import gcd 

def co_prime(a,b): 
    return gcd(a,b) == 1 
a = int(input())
b = int(input())
if co_prime(a,b):
    print("Coprime")
else:
    print("Prime")