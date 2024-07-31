def main():
    print("Holy shit it I'm going to fucking explode")
    print("(1), Run for the bathroom")
    print("(2), just shit everywhere")

    choice = input("Make your choice: ")
    if choice == '1':
            print("you run to the nearest lady to ask where the nearest bathroom is")
            print("You're struggling to put your request into words, what do you say?")
            path1();

    if choice == '2':
            print("You shit everywhere")
            print("I hope you're happy")
            restart();

def path1():
    import random
    print("(1), shit on the lady")
    print("(2), RISK: ask the lady out")
    print("(3), ask where the bathroom is")
    choice = input("Make your choice ")
    if choice == '1':
        print("You shat all over the lady")
        print("I hope you're happy")
        restart();
    if choice == '2':
        random_integer = random.randint(1, 2)
        if random_integer == 1:
            print("She said yes!")
            restart();
        else:
            print("She pepper sprayed you and you shat everywhere")
            print("I hope you're happy")
            restart();

    if choice == '3':
        print("You Shat in the toilet yay")
        restart();

def restart():
    print("type Y to restart")
    choice = input("here: ")
    if choice in['Y', 'y']:
        main();    
main()
