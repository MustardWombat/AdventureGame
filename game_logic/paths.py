RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
stat = ''
health = 0
coin = 0
reset = 0

def path0():
    global health
    int()
    print("You see a cave while hiking, what do you do?")
    print(f"{BLUE}(1) Enter the cave")
    print("(2) Give up, I'm not the adventurous type")

    choice = input(f"{RESET}Make your choice: ")
    if choice == '1':
        int()
        path1()
    elif choice == '2':
        int()
        print("You turned back home, and you never know what lies in the cave.")
        functions.restart()
    else:
        int()
        print("Invalid choice. Please select 1 or 2.")
        path0()
