print("Don't blow up the computer.")
print("Want to play a round of blackjack.")

userInput = input(" ")

#Deal out cards
#Calculate payout
def idk():
    if "yes" or "Yes" in userInput:
        #Let the player deciede, but if it is a high number then yell at player
        print("How much do you want to loan out?")
        userInput = input(" ")
    
    #Limit player at 10,000
    if int(userInput) > 10000:
        print("Isn't that a tad much, let's ask for a lower number.")
        return idk
   
        