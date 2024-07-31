# Declare stat as a global variable
stat = ''

def main():
    global stat  # Tell Python that we're using the global variable stat
    print("Welcome adventurer, who would you like to be?")
    print("(1), Fast and athletic")
    print("(2), Clever and smart")
    print("(3), Strong and durable")
    choice = input("Make your choice: ")
    if choice == '1':
        stat = 'fast'
        path0()
    elif choice == '2':
        stat = 'clever'
        path0()
    elif choice == '3':
        stat = 'strong'
        path0()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        main()

def path0():
    print("You see a cave while hiking, what do you do?")
    print("(1), Enter the cave")
    print("(2), Give up, I'm not the adventurous type")

    choice = input("Make your choice: ")
    if choice == '1':
        print("You enter the cave, you see a door, but it's locked.")
        print("You also see an old bridge over a ravine")
        path1()
    elif choice == '2':
        print("You turned back home, and you never know what lies in the cave.")
        print("I hope you're happy")
        restart()
    else:
        print("Invalid choice. Please select 1 or 2.")
        path0()

def path1():
    import random
    print("(1), Turn back, this is too scary")
    print("(2), RISK: Pick the lock")
    print("(3), RISK: Take the old bridge")
    choice = input("Make your choice: ")
    if choice == '1':
        print("You turned back home, and you never know what lies beyond the cave.")
        print("I hope you're happy")
        restart()
    elif choice == '2':
        if stat == 'clever':
            print("Using your clever by nature mind, this was no challenge to you")
            print("You successfully picked the lock!!")
            restart()
        elif stat == 'fast':
            print("Your fast nature caused you to rush the process")
            print("Your lockpick snapped, and the cave closed the entrance, locking you inside forever")
            print("I hope you're happy")
            restart()
        elif stat == 'strong':
            print("your brute hands arent capable of anything besides destroying")
            print("Your lockpick snapped, however, you just smashed the door open in anger, letting you inside")
            restart()
        else:
            random_integer = random.randint(1, 2)
            if random_integer == 1:
                print("You successfully picked the lock!!")
                restart()
            else:
                print("Your lockpick snapped, and the cave closed the entrance, locking you inside forever")
                print("I hope you're happy")
                restart()
    elif choice == '3':
        random_integer = random.randint(1, 2)
        if random_integer == 1:
            print("You barely make the bridge before it falls apart behind you")
            restart()
        else:
            print("You fell off the bridge")
            print("I hope you're happy")
            restart()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        path1()

def restart():
    print("Type Y to restart")
    choice = input("Here: ")
    if choice in ['Y', 'y']:
        main()
    else:
        print("Exiting the game.")
        exit()

main()