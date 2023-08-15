#to avoid defining functions at top

def main():
    name = ask() #scope of variable name is limited to main function
    hello(name)
    hello()

def ask():
    user = input("What's your name ? ")
    return user

def hello(to = "World"):  
    print("hello,", to)


main()