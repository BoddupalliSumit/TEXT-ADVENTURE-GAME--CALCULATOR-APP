
# text_adventure_game.py

def intro():
    print("\n🏰 Welcome, brave adventurer! 🌄")
    name = input("What is your name, hero? ")
    print(f"\nHello {name}, your journey begins now.")
    start_adventure()

def start_adventure():
    print("\nYou're standing at the edge of a dark forest. 🌲🌲")
    print("1. Enter the forest")
    print("2. Walk along the forest edge")
    print("3. Rest under a tree")
    choice = input("Choose an action (1/2/3): ")
    if choice == "1":
        forest_path()
    elif choice == "2":
        edge_path()
    elif choice == "3":
        rest_area()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

def forest_path():
    print("\nYou step into the dark forest. It's quiet... too quiet.")
    print("1. Investigate the sound")
    print("2. Hide behind a tree")
    choice = input("Choose an action (1/2): ")
    if choice == "1":
        print("\nA wild wolf appears! 🐺 You fight it bravely.")
        inventory.append("Wolf Fang")
        print("You obtained: Wolf Fang")
        find_sword()
    elif choice == "2":
        print("\nYou hide safely and avoid danger, but miss the chance to collect anything.")
        find_sword()
    else:
        print("Invalid choice.")
        forest_path()

def edge_path():
    print("\nYou find a small chest hidden in the grass.")
    print("1. Open it")
    print("2. Ignore it and continue walking")
    choice = input("Choose an action (1/2): ")
    if choice == "1":
        print("\nYou found a health potion! 🧪")
        inventory.append("Health Potion")
        cave_entrance()
    elif choice == "2":
        print("\nYou walk away and find a mysterious cave entrance.")
        cave_entrance()
    else:
        print("Invalid choice.")
        edge_path()

def rest_area():
    print("\nYou rest under a tree and regain some strength. 🌳")
    print("But suddenly, a bandit appears!")
    print("1. Fight with bare hands")
    print("2. Try to bribe him with gold (you have none)")
    choice = input("Choose an action (1/2): ")
    if choice == "1":
        print("\nYou bravely fight and defeat the bandit! 💪")
        inventory.append("Gold Coin")
        cave_entrance()
    elif choice == "2":
        print("\nHe realizes you have no gold and attacks you! You flee barely alive.")
        find_sword()
    else:
        print("Invalid choice.")
        rest_area()

def find_sword():
    print("\nYou find a glowing sword stuck in a rock. ⚔️")
    print("1. Try to pull it out")
    print("2. Ignore it and walk past")
    choice = input("Choose an action (1/2): ")
    if choice == "1":
        print("\nYou pull hard... and it comes loose! You have the Magic Sword! 🔥")
        inventory.append("Magic Sword")
        cave_entrance()
    elif choice == "2":
        print("\nYou walk past the sword. It might have been useful...")
        cave_entrance()
    else:
        print("Invalid choice.")
        find_sword()

def cave_entrance():
    print("\nYou arrive at the mouth of a dark cave. 🕳️")
    print("1. Enter the cave")
    print("2. Camp outside")
    choice = input("Choose an action (1/2): ")
    if choice == "1":
        final_battle()
    elif choice == "2":
        print("\nWhile camping, you are ambushed by goblins and lose your inventory!")
        inventory.clear()
        final_battle()
    else:
        print("Invalid choice.")
        cave_entrance()

def final_battle():
    print("\nInside the cave, a Dragon awaits! 🐉")
    if "Magic Sword" in inventory:
        print("You draw your Magic Sword... and defeat the Dragon in a fierce battle! 🏆")
        inventory.append("Dragon Scale")
        end_game(True)
    else:
        print("You try to fight with bare hands, but it's no use. The Dragon defeats you. 💀")
        end_game(False)

def end_game(victory):
    print("\n🎉 Adventure Complete!")
    if victory:
        print("You are a true hero! 🏅")
    else:
        print("You fought bravely. Better luck next time.")
    print("Your final inventory:", inventory)

# Start the game
inventory = []
intro()
