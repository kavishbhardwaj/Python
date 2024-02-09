name = input("What's your name? ")

match name: 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                     # _ is used in other contexts also. Here, it acts as "else" 
        print("Who?")