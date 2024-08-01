import random

# Declare global variables
stat = ''
health = 0

def print_if_changed(new_health):
    global health
    
    # Check if the health value has changed
    if new_health != health:
        print(f"Health changed to: {new_health}")
        health = new_health

def main():
    global stat, health  # Use global variables
    
    print("Welcome adventurer, who would you like to be?")
    print("(1), Fast and athletic")
    print("(2), Clever and smart")
    print("(3), Strong and durable")
    print("(4), Lucky")

    choice = input("Make your choice: ")
    if choice == '1':
        stat = 'fast'
        health = 6
    elif choice == '2':
        stat = 'clever'
        health = 9
    elif choice == '3':
        stat = 'strong'
        health = 12
    elif choice == '4':
        stat = 'lucky'
        health = 9
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        main()
        return  # Exit to avoid further execution if choice is invalid

    path0()

def path0():
    global health
    
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
    print("(1), Turn back, this is too scary")
    print("(2), RISK: Pick the lock")
    print("(3), RISK: Take the old bridge")
    
    choice = input("Make your choice: ")
    if choice == '1':
        print("You turned back home, and you never know what lies beyond the cave.")
        print("I hope you're happy")
        restart()
    elif choice == '2':
        handle_lock_pick()
    elif choice == '3':
        handle_bridge()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        path1()

def handle_lock_pick():
    global stat
    if stat == 'clever':
        print("Using your clever by nature mind, this was no challenge to you")
        print("You successfully picked the lock!!")
        patha0()
    elif stat == 'fast':
        if random.randint(1,2) == 1:
            print("You successfully picked the lock!!")
            patha0() 
        else:
            print("Your fast nature caused you to rush the process, you injure yourself")
            print_if_changed(health - 2)  # Update health and print if changed
            path1()
    elif stat == 'lucky':
        if random.randint(1, 10) >= 2:
            print("You successfully picked the lock!!")
            patha0()
        else:
            print("Your lockpick snapped, and the cave closed the entrance, locking you inside forever")
            print("I hope you're happy")
            restart()
    else:
        if random.randint(1, 2) == 1:
            print("You successfully picked the lock!!")
            patha0()
        else:
            print("Your lockpick snapped, and the cave closed the entrance, locking you inside forever")
            print("I hope you're happy")
            restart()

def handle_bridge():
    if random.randint(1, 2) == 1:
        print("You barely make the bridge before it falls apart behind you")
        restart()
    else:
        print("You fell off the bridge")
        print("I hope you're happy")
        restart()

def patha0():
    print('You made it past the door to the treasure!')
    restart()

def restart():
    print("Type Y to restart")
    choice = input("Here: ")
    if choice in ['Y', 'y']:
        main()
    else:
        print("Exiting the game.")
        exit()

main()