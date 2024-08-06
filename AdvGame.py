import random

# Declare global variables
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
stat = ''
health = 0
coin = 0

def healthchange(new_health):
    global health
    # Check if the health value has changed
    if new_health != health:
        health = new_health

def coinchange(new_coin):
    global coin
    # Check if the coin value has changed
    if new_coin != health:
        coin = new_coin


def main():
    global stat, health, coin  # Use global variables
    int()
    print("Welcome adventurer, who would you like to be?")
    print("(1) Fast and athletic")
    print("(2) Clever and smart")
    print("(3) Strong and durable")
    print("(4) Lucky")

    choice = input("Make your choice: ")
    if choice == '1':
        stat = 'fast'
        health = 6
        coin = 2
    elif choice == '2':
        stat = 'clever'
        health = 9
        coin = 10
    elif choice == '3':
        stat = 'strong'
        health = 12
        coin = 2
    elif choice == '4':
        stat = 'lucky'
        health = 9
        coin = 10
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        main()
        return  # Exit to avoid further execution if choice is invalid

    path0()

def path0():
    global health
    int()
    print("You see a cave while hiking, what do you do?")
    print("(1) Enter the cave")
    print("(2) Give up, I'm not the adventurous type")

    choice = input("Make your choice: ")
    if choice == '1':
        int()
        print("You enter the cave, you see a door, but it's locked.")
        print("You also see an old bridge over a ravine")
        path1()
    elif choice == '2':
        int()
        print("You turned back home, and you never know what lies in the cave.")
        restart()
    else:
        int()
        print("Invalid choice. Please select 1 or 2.")
        path0()

def path1():
    int()
    print("(1) Turn back, this is too scary")
    print("(2) RISK: Pick the lock")
    print("(3) RISK: Take the old bridge")
    
    choice = input("Make your choice: ")
    if choice == '1':
        print("You turned back home, and you never know what lies beyond the cave.")
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
        print("Using your clever nature, this was no challenge to you")
        print("You successfully picked the lock!!")
        patha0()
    elif stat == 'fast':
        if random.randint(1, 2) == 1:
            print("You successfully picked the lock!!")
            patha0() 
        else:
            print("Your fast nature caused you to rush the process, you injure yourself")
            healthchange(health - 2)  # Update health and print if changed
            path1()
    elif stat == 'lucky':
        if random.randint(1, 10) >= 2:
            print("You successfully picked the lock!!")
            patha0()
        else:
            print("Your lockpick snapped, and the cave closed the entrance, locking you inside forever")
            restart()
    else:
        if random.randint(1, 2) == 1:
            print("You successfully picked the lock!!")
            patha0()
        else:
            print("Your lockpick snapped, and the cave closed the entrance, locking you inside forever")
            restart()

def handle_bridge():
    if stat == 'fast':
        print("You are fast, and you make it across the bridge safely.")
        pathb0()
    elif random.randint(1, 2) == 1:
        print("You barely make the bridge before it falls apart behind you")
        path0b()
    else:
        print("You fell off the bridge")
        restart()

def patha0():
    print('You made it past the door to the treasure!')
    coinchange(coin + 6)
    path0()

def pathb0():
    print('Past the bridge you see a tomb with a puzzle')
    print('I am related to coding, what am I?')
    
    def display_word(word, guessed_letters):
        return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

    def get_word():
        words = ["python", "hangman", "challenge", "programming", "development"]
        return random.choice(words)
    
    def hangman():
        global health
        word = get_word().upper()  # Get the word and convert it to uppercase
        guessed_letters = set()
        incorrect_guesses = 0
        max_attempts = 6

        print("Welcome to Hangman!")
        print(f"The word has {len(word)} letters.")

        while incorrect_guesses < max_attempts or health > 0:
            print(display_word(word, guessed_letters))
            guess = input("Guess a letter: ").upper()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            
            if guess in word:
                guessed_letters.add(guess)
                if all(letter in guessed_letters for letter in word):
                    print(f"Congratulations! You guessed the word: {word}")
                    break
            elif max_attempts - incorrect_guesses >= 1:
                incorrect_guesses += 1
                print(f"Incorrect guess. You have {max_attempts - incorrect_guesses} attempts left.")
            if incorrect_guesses - max_attempts == 0:
                print("a trap activated, shooting you with an arrow")
                healthchange(health - 1)  # Deduct health on incorrect guess

        if health <= 0:
            print(f"Game over. The word was: {word}")
        restart()
    
    hangman()

def path0b():
    print("This path leads to a dead end.")
    print("I hope you're happy")
    restart()

def restart():
    print("I hope you're happy...")
    print("")
    choice = input("Type Y to restart: ")

    if choice.upper() == 'Y':
        global health
        health = 0  # Reset health
        main()
    else:
        print("Exiting the game...")
        exit()

def int():
    print('')
    if health != 0:
        health_display = f"{RED}|{RESET}" * health
        print(f"HEALTH: {health_display}")
    if coin != 0:
        coin_display = f"{YELLOW}0{RESET}" * coin
        print(f"COINS: {coin_display}")
main()
