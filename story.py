def intro():
    print("You wake up in a dark forest. You can go left, right, or center.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")


def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("Summoning your courage, you pull it free and feel unstoppable power surge through you.")
    print("With the sword in hand, you defeat the dragon guarding the forest and restore peace.")
def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")


def center_path():
    print("You walk straight ahead and discover a glowing portal that hums with strange energy.")


if __name__ == "__main__":
    intro()
