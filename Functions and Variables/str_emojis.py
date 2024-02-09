def main():
    user_input = input('''Enter a sentence 
    with emoticons: ''')
    print(convert(user_input))

# https://docs.python.org/3/howto/unicode.html

def convert(emoticon):
    emoticon = \
                 emoticon.replace(":)", "\U0001F642") \
                                                      .replace(":(" , "\U0001F641")
    
    # line continuation character, a backslash ( \ ) 

    print(len(emoticon))   # length of string len()
    return emoticon

main()


#    https://unicode.org/emoji/charts/full-emoji-list.html emojis