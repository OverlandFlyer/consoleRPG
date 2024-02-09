#This will be all the rooms and objects within them
def roomInputs(roomNumber, lightsOn):
    if(roomNumber == 1): #This will be your apartment, starting room
        if(lightsOn == True):
            print("You are in your apartment. You see your door, window, and fridge.")
        else:
            print("You are not able to see anything in this darkness. Maybe you should turn on a light.")
    if(roomNumber == 2): #This will be your neighbor's apartment, where you find food
        if(lightsOn == True):
            print("This is your neighbors apartment, it is. There is a medium-sized hole in the sidewall, fridge, window, and lamp.")
        else:
            print("You are not able to see anything in this darkness. Maybe you should turn on a light.")
    if(roomNumber == 3):
        print("You find yourself in an armory. It seems like someone beat you here leaving you with only a shield and club. There is another door but as you get closer you hear music through it. It is some of the most beautiful and calming music you've ever heard. The music draws you closer to the door. You open the door and find yourself in a concert hall now.") #Jim Jun Dun final boss, final phase
    if(roomNumber == 4): #Maze begins
        print("There isn't anything in here. It's just an empty room with nothing except ")
        
    else:
        roomNumber = 0 #In the hallway the lights will reset, you might find enemies, or find items/food and weapons
        print("You find yourself in the hallway.")
    
#Add in background story
userInput = input("> ")

#This is all possible input player is able to use for a result
def allInputs():
    for s in userInput:
        if 'door' in s:
            roomInputs
        if 'look' in s:
            print(roomInputs(roomNumber=currentRoom, lightsOn=checkingLights))
        if 'fridge' in s:
            roomInputs
                     
#This will turn on the lights and if they are on you will be able to see the room
def checkingLights(): 
    for s in userInput:
        if 'lights' in s:
            if(roomInputs(roomNumber=currentRoom, lightsOn=True)):
                print("The lights are already on.")
                return True
            if(roomInputs(roomNumber=currentRoom, lightsOn=False)): 
                print("You turn on the lights and now able to see what's around you.")
                return True
            if(roomInputs(roomNumber=0)): #Whenever you enter the hallway it will reset the lights to be off
                return False
            