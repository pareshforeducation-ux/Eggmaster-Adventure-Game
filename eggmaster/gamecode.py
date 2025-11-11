import os
import random

# Always run in the folder where story.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

HP = 100
inventory = []
dead = False

# --- Flags for tracking key decisions ---
followed_monkeys = False
explored_cave = False
checked_mushroom = False
scouted_tree = False
crossed_river = False
picked_herbs = False
avoided_noise = False
swung_vine = False
risky_jump = False
met_hermit = False
entered_temple = False

# --- Functions ---
def read_story(filename):
    try:
        with open(filename, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return f"[Missing file: {filename}]"

def print_slow(text):
    print("\n" + text + "\n")

def change_hp(amount):
    global HP, dead
    HP += amount
    print(f"Your HP is now {HP}.")
    if HP <= 0:
        dead = True
        lose_game("HP dropped to zero.")

def show_ending(filename=None, story_text=None):
    if story_text:
        story = story_text
    else:
        story = read_story(filename)
    print_slow(story)
    with open("story_output.html", "w") as f:
        f.write(f"<html><head><link rel='stylesheet' href='style.css'></head><body><div class='story'>{story}</div></body></html>")
    print("\n✅ Story exported to story_output.html")

# --- Helper to show status ---
def show_status():
    print(f"\nCurrent HP: {HP}")
    print(f"Inventory: {inventory}")

# --- Lose function ---
def lose_game(reason):
    global HP, inventory
    lose_text = f"💀 Alas, Mr. Eggmaster! {reason}\nHP: {HP}\nInventory: {inventory}\n"
    show_ending(story_text=lose_text)
    exit()

# --- Start of Jungle Adventure ---
print_slow(read_story("jungle_1.txt"))
choice1 = input("Choose (1/2/3): ").strip()

if choice1 == "1":
    print_slow("You follow the monkeys and discover some magical berries. 🍇 HP +10")
    change_hp(10)
    inventory.append("Magical Berries")
    followed_monkeys = True
elif choice1 == "2":
    print_slow("You explore the cave and find a small healing herb. HP +5")
    change_hp(5)
    inventory.append("Healing Herb")
    explored_cave = True
elif choice1 == "3":
    if random.random() < 0.25:
        lose_game("You ate a glowing mushroom out of curiosity... fatal mistake!")
    else:
        print_slow("You carefully avoid the mushrooms and find a shiny compass!")
        inventory.append("Compass")
        checked_mushroom = True
else:
    lose_game("You wandered aimlessly and got lost in the jungle!")

show_status()

# --- Decision 2 ---
print_slow(read_story("jungle_2.txt"))
choice2 = input("Choose (1/2): ").strip()

if choice2 == "1":
    print_slow("You carefully cross the river on slippery logs. HP -10 but you succeed.")
    change_hp(-10)
    crossed_river = True
elif choice2 == "2":
    print_slow("Climbing the tall tree, you scout a safer path. No HP lost.")
    scouted_tree = True
else:
    lose_game("Unable to make a safe choice, you fall into the river and perish!")

show_status()

# --- Decision 3 ---
print_slow(read_story("jungle_3.txt"))
choice3 = input("Choose (1/2/3): ").strip()

if choice3 == "1":
    print_slow("You pick the herbs and restore 10 HP.")
    change_hp(10)
    inventory.append("Healing Herbs")
    picked_herbs = True
elif choice3 == "2":
    print_slow("You carefully follow the narrow path avoiding hidden traps. No HP lost.")
elif choice3 == "3":
    if random.random() < 0.20:
        lose_game("Investigating the shiny object triggers a hidden trap. Instant death!")
    else:
        print_slow("The shiny object is a compass fragment! You add it to your inventory.")
        inventory.append("Compass Fragment")
else:
    lose_game("You got distracted and fell into a trap!")
# --- Decision 4 ---
print_slow(read_story("jungle_4.txt"))
choice4 = input("Choose (1/2/3): ").strip()

if choice4 == "1":
    print_slow("You swing across a ravine using a vine. HP -5 but you succeed.")
    change_hp(-5)
    swung_vine = True
elif choice4 == "2":
    print_slow("You carefully walk around the ravine, taking extra time. No HP lost.")
elif choice4 == "3":
    if random.random() < 0.25:
        lose_game("You attempt a risky jump and fall! Instant death!")
    else:
        print_slow("Your risky jump surprisingly works! You feel exhilarated.")
        risky_jump = True
else:
    lose_game("Indecision leads you to fall into the ravine!")

show_status()

# --- Decision 5 ---
print_slow(read_story("jungle_5.txt"))
choice5 = input("Choose (1/2): ").strip()

if choice5 == "1":
    print_slow("You meet a hermit who teaches survival tricks. HP +5")
    change_hp(5)
    met_hermit = True
elif choice5 == "2":
    print_slow("You avoid the hermit and continue. No HP lost.")
    avoided_noise = True
else:
    lose_game("You disturb the hermit’s trap and perish!")

show_status()

# --- Decision 6 ---
print_slow(read_story("jungle_6.txt"))
choice6 = input("Choose (1/2/3): ").strip()

if choice6 == "1":
    print_slow("You carefully enter the ancient temple and find a treasure map!")
    inventory.append("Treasure Map")
    entered_temple = True
elif choice6 == "2":
    print_slow("You avoid the temple to stay safe. No HP lost.")
elif choice6 == "3":
    if random.random() < 0.20:
        lose_game("You triggered a booby trap inside the temple! Fatal!")
    else:
        print_slow("You sneak past traps and collect a golden idol.")
        inventory.append("Golden Idol")
else:
    lose_game("You wander carelessly into traps and perish!")

show_status()

# --- Decision 7 ---
print_slow(read_story("jungle_7.txt"))
choice7 = input("Choose (1/2): ").strip()

if choice7 == "1":
    print_slow("You finally reach the treasure! Victory is yours! 🏆")
    # Dynamic Win Ending
    win_ending = "🎉 Congratulations, Mr. Eggmaster! You survived the Amazon jungle.\n"
    if followed_monkeys:
        win_ending += "Following the monkeys helped you discover magical berries. 🍇\n"
    if explored_cave:
        win_ending += "Exploring the cave gave you a healing herb. 🌿\n"
    if checked_mushroom:
        win_ending += "Careful steps past mushrooms saved you from danger. 🍄\n"
    if crossed_river:
        win_ending += "Braving the river added to your survival skills. 🌊\n"
    if scouted_tree:
        win_ending += "Scouting from the tree gave a safer path. 🌳\n"
    if picked_herbs:
        win_ending += "Collecting herbs kept your HP high. 🌿\n"
    if swung_vine:
        win_ending += "Swinging across the ravine tested your agility. 🌉\n"
    if risky_jump:
        win_ending += "The risky jump proved your bravery. 🪂\n"
    if met_hermit:
        win_ending += "The hermit’s guidance was invaluable. 🧙‍♂️\n"
    if entered_temple:
        win_ending += "The temple treasures aided your adventure. 🏛️\n"
    win_ending += f"Final HP: {HP}\nInventory: {inventory}\n"
    show_ending(story_text=win_ending)

elif choice7 == "2":
    lose_game("You hesitated at the final moment and got lost! The treasure remains hidden.")

else:
    lose_game("A strange choice leads you astray... you are lost forever!")

# End of Jungle Adventure
