#Finding whether a number is even or odd 
#The modulo % operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False      #Pythonic way; % means modulo
    # return n % 2 == 0                       #Alternate way to perfrom same function

main()