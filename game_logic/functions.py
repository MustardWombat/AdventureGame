def restart():
    print("I hope you're happy...")
    print("")
    choice = input("Type Y to restart: ")

    if choice.upper() == 'Y':
        global health
        global coin
        global reset
        health = 0  # Reset health
        coin = 0
        return True
            
    else:
        print("Exiting the game...")
        exit()
