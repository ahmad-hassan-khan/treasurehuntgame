# ..............................................................................
# ..................TREASURE HUNT GAME ..............................................
print('''
*******************************************************************************
            ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   
             \-P-A-K-I-S-T-A-N\_&_/--E_G_Y_P_T-/-__/
              |===\!/========================\!/===|
              |   |=|  P A  T  .---. T A W   |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |_|_|===AHMAD HAS) V (SAN KHAN===|-|_|
              |__|___|___|__|__)uuu(|__|___|___|__-|
              -x-x-x-x-x-x-x-xx-x--x-x-x-x-x-x-x-x-x
*******************************************************************************
''')
print("Welcome to Treasure Island\nYour Mission is to Find the Treasure\n")
choice1 = input('You are at the crossroad ,where do you want to go.Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake.There os a island in the middle of the lake.Type "wait"to wait for the boat.Type "swim" to sim across\n').lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed.There is house with 3 doors.One red,one yellow and one blue.Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("Its room full of fire.Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure you won!")
        elif choice3 == "blue":
            print("You enter a room of beasts.Game over!")
    else:
        print("You chosen the wrong door.Game over!")
