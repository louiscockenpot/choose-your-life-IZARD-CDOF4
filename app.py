

def introduction():
    print("Welcome to the Forest Adventure Game!")
    print("You wake up in your vacation house, ready for your usuall morning run.")
    print("Your goal is to make decisions that will lead you out of the forest and back to your home safe.\nGood Luck!")

def choose_path():
    print("\nYou come across an intersection on the way. Which path do you choose?")
    print("1. Take the left path.")
    print("2. Take the right path.")
    return input("Enter 1 or 2: ")

def explore_meadow():
    print("\nYou chose the left path.")
    print("You continue running. As you follow the left path, you discover a beautiful meadow with lots of flowers.")
    print("What do you want to do?")
    print("1. Take a moment to enjoy the meadow.")
    print("2. Continue running without stopping.")
    return input("Enter 1 or 2: ")

def encounter_enemy():
    print("\nOh no! You encounter a wild animal.")
    print("What do you want to do?")
    print("1. Try to scare it away.")
    print("2. Slowly back away.")
    return input("Enter 1 or 2: ")

def shortcut_choice():
    print("You seem to find a shortcut through the forest")
    print("What do you want to do?")
    print("1. Take the shortcut.")
    print("2. Keep running on the meadow path.")
    return input("Enter 1 or 2: ")

def resolution(outcome):
    if outcome == "win":
        print("\nCongratulations! You successfully got out of the forest and completed your morning run.")
    else:
       print("\nOops! Your adventure stops here, you're dead. Better luck next time!")



def forest_adventure():
    introduction()

    path_choice = choose_path()

    
    if path_choice == "1":
        print("\nYou chose the left path.")
       
        explore_choice = explore_meadow()

        if explore_choice == "1":
            print("Unfortunatly you remember that you are allergic to pollen and you choke to death.")
            resolution("lose")
        elif explore_choice == "2":
            print("You decide to continue running without stopping.")
            shortcut =shortcut_choice()
            if shortcut == "1": 
                print("Why would you want to go back in the forest. It's scary and weird people hiddes in it.")
                print("A psyco stabbs you to death :(")
                resolution("lose")


            elif shortcut =="2": 
                print("Clever choice ! Plus it smells nice ")
                resolution("win")

        else:
            print("\nInvalid input. Your indecision leads to an unfortunate outcome.")
            resolution("lose")

    elif path_choice == "2":
        print("\nYou chose the right path.")

        enemy_choice = encounter_enemy()
        if enemy_choice == "1":
            print("You successfully scare away the wild animal and continue your run.")
            resolution("win")
        else:
            print("The wild animal blocks your way, and jumps on you.")
            resolution("lose")
    else:
        print("\nInvalid input. Your indecision leads to an unfortunate outcome.")
        resolution("lose")

if __name__ == "__main__":
    forest_adventure()
