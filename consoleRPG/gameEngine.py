from ast import In
import random

print("Hello, choose a character.")
print("Fighter or climber")
userInput = input("> ")

print("You wake up and you are in the middle of what seems to be a never ending hallway.")
print("Which way do you go.")
userInput = input("> ")
if('fighter' or 'climber' in userInput):
    routeOne(0,0)


#This is all possible input player is able to use for a result
def routeOne(currentRoom, roomNumber):
    userInput
    for s in userInput:
        if 'north' in s and currentRoom <= 8:
            print("It's quiet. You hear nothing except your footsteps. You find a door but upon trying it, you find it is locked.")
            currentRoom = roomNumber + 1
            break
        if 'north' in s and currentRoom == 8:
            print("Heard something. You hear a noise from the door to your left. As you get closer it stops, you try the door and this one isn't locked.")    
            currentRoom = roomNumber + 1
            break
        if 'north' in s and currentRoom == 9:
            print("It's not quiet anymore. You hear noises all around you. Each room has something behind it now. The doors are trying to open, you need to run.")
            currentRoom = roomNumber + 1
            break
        if 'north' in s and currentRoom >= 10:
            print("Keep going. They are still trying to get you.")
            currentRoom = roomNumber + 1
            break
        if 'north' in s and currentRoom == 12:
            print("You can't go any further. Something is stopping you. All you see is brightness, you can't see what it is but it's in your way. You must remove it.")
            userInput = input("> ")
            if 'fight' is s and currentRoom == 12:
                chance = random.randint(1,3)
                if chance == 1:
                    print("You swing blindly at the light and you feel it jolt back in shock.")
                    print("Do you try to swing again")
                    userInput("> ")
                    if 'yes' in s:
                        chance = random.randint(1,3)
                        if chance == 1:
                            print("You got lucky and hit in the right spot it seems because it falters and fades.")
                            print("You can see the end. You see an exit sign and run to it. It opens to reveal a empty field. No clouds, trees, or even wind. It seems that you are the only thing here. It's rather peaceful though.")
                            exit()
                        if chance == 2:
                            print("You swing again but this time it was ready. It flashed another blinding light so you couldn't see. You move in a backward to keep distance.")
                            print("Do you swing again")
                            break
                        if chance == 3:
                            print("You swing and feel it connect but it doesn't seem to be scared anymore. This time it swings back but as it swings you feel a burning sensation. Last thing you see the bright light as you burn alive.")
                            print("You were burnt alive. Killed by the Light.")
                            exit()
                if chance == 2:
                    print("You swing but completely wiff it hitting a door. You're able to hit it hard enough for the break down. You hear something running out but just as you hear that you see the light flash and it's gone. It seemed to have stopped the beast, protecting you.")
                    print("Should you swing again, it did protect you.")
                    if 'yes' in s:
                        print("Just as you raise your fist to swing you hear a loud humming. You look around to find what is making it but instead, you see every single door has now opened up. You turn back to the light but it's vanished, leaving you to fight them all yourself.")
                        print("You weren't able to fight the horde of beast. Killed by the horde.")
                        exit()
                    if 'no' in s:
                        print("You thank the light. It dims down to reveal a wall with a door. It slowly fades enough to allow you to walk through it. You walk through opening the door. It holds nothing but snowed over mountian top. It is steep but there is a path and a shelter in front of you.")
                        print("You turn back to see nothing is there. The door is gone, leaving you to just walk to the shelter instead. You can begin to live a more peaceful live.")
                        exit()
                if chance == 3:
                    print("You follow up with a full combo. It just moves further and further back the more you hit it. It doesn't show any sort of resistance but it does feel like it's getting brighter with each hit. It gets so bright you eventually are unable to swing anymore. Once you are able to see again, you aren't in the hallway anymore and the light is no where to be seen. You are able to just see these weird orange scribbles on the walls. You aren't able to understand them but when you touch one you see a red snake appear after you touch it and feel a great earthquake.")
                    print("You got crushed by the orange scribbles. Killed by magic maybe?")
                    exit()
            else:
                print("You should fight it.")
                break
        if 'west' in s and roomNumber == 8:
            print("You enter the room and see a hammer to your right. You grab it to be safe. As you grab it you hear something in the other room and then something lunges at you.")
            chance = random.randint(1,2)
            if chance == 1:
                print("You swing with your hammer it kills the beast. You run back into the hall.")
                break
            if chance == 2:
                print("You swing and you miss. It stabs you. You beat it dead but you aren't going to make it either.")
                print("You were stabbed. Killed by just a knife.")
                exit()
        else:
            print("Input not understood. Try again")
            break
            
            