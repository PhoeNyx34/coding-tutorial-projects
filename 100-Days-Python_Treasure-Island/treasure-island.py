print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

crossroad = input("You're at a crossroads. Which direction do you want to go? Type 'left' or 'right': ")
if crossroad == 'left' or crossroad.lower() == 'l':
    lake = input("You come to a lake with an island in the middle. Do you want to wait for a boat or swim across? Type 'wait' or 'swim': ")
    if lake == 'wait' or lake.lower() == 'w':
        door = input("You arrive at the island unharmed. There is a house with three doors: one red, one yellow, and one blue. Which door do you open? Type 'red', 'yellow', or 'blue': ")
        if door == 'red' or door.lower() == 'r':
            print("You spontaneously burst into flames.\nGame over.")
        elif door == 'blue' or door == 'b':
            print("You're eaten by starved beasts.\nGame over.")
        elif door == 'yellow' or door == 'y':
            print("You've found the treasure!")
        else:
            print("You're swallowed by black void of indecision.\nGame over.")
    else:
        print("You're attacked by a school of pike.\nGame over.")    
else:
    print("You fall into a hole.\nGame over.")