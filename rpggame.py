#need to finish story
#need to link shit for example when you leave dungeon you go to pathway2 and when you finish exploring dungeon go to pathway or what ever imma add later
#need to add point system but got no clue how to
import math
print("Words inside of brackets [ ] are your possible options")
print("Welcome to treasure hunt game")


def CreateText(text):
    return input(text + "\n")

def IncrementPoints(amount):
    points = 0
    
    points += amount

#pathway = input("You see a pathway. Do you want to go left or right?\n ")
pathway = CreateText("You see a pathway. Do you want to go [left] or [right]?")
#return function ikea way
while pathway != "left":
    print("You chose the wrong path and you already failed your adventure...")
    pathway = CreateText("You see a pathway. Do you want to go [left] or [right]?")
    
if pathway.lower() == "left":
    river = CreateText("You chose the right path! Now you see a river, will you [jump] over or [swim]?")
    if river.lower() == "jump":
        print("You jumped over a river full of aligators, your adventure continues")
        dragon = CreateText("You see a dragon, do you want to attack with [fire], [ice] or [wind] magic?")
        if dragon.lower() == "fire":
            print("Dragon took critical damage and died instantly")
        elif dragon.lower() == "ice":
            print("Dragon froze to death")          
        if dragon.lower() != "wind" and dragon.lower() == "fire" or dragon.lower() == "ice":
            dungeon = CreateText("After killing the dragon you see a pathway leading to a dungeon. Do you want to enter it?  [yes] [no]")
            if dungeon.lower() == "yes":
                print("You came across a great treasures")
                crown = CreateText("You found a crown that was once worn by the greatest dragon kings of all time. What do you do with it? [wear] it or [leave] it where it was?")
                if crown.lower() == "wear":
                    print("You put the crown on and you gain +5 Points")
                    IncrementPoints(5)
                    explore = CreateText("Do you want to leave the cave or explore it deeper? [leave] It/[explore] Deeper")
                    if explore.lower() == "leave":
                        print("You left the dungeon and you continuing your adventure on the pathway")
                        print("Game is not finished and you cannot continue further")
                    if explore.lower() == "explore":
                        print("Good choice, you continue exploring the dungeon and you find a secter door. What do you do? [open] the door or [leave] the dungeon\n")
                        print("Game is not finished and you cannot continue further")
                elif crown.lower() == "leave":
                    print("You left a great treasure and left the dungeon.")
            elif dungeon.lower() == "no":
                print("You are afraid, you choose to go further down the pathway")
                pathway2 = CreateText("You are continuing your advanture and you stumble across a group of unknown people. What you do? [Run] away, [Talk] with them, [Hide] in nearby bushes")
                if pathway2.lower() == "run":
                    print("As you were running you ran into a boogy trap and now you are wounded. -4 Points")
                    IncrementPoints(-4)
                    print("Game is not finished and you cannot continue further")
                elif pathway2.lower() == "talk":
                    print("They seem friendly and they offer you a quest for a great rewards")
                    print("They brought you to their small village to meet the elders of the village")
                    print("You talk with the elders for a little bit, and they see your crown and starts asking about it")
                    quest = CreateText("After some time they offer you a quest to retrieve a sword once used by the kings that once wore the crown. Do you [accept] the quest or do you [decline] it?")
                    if quest.lower() == "accept":
                        print("You accepted the quest and one of the elders gave you a map where you can find the sword")
                    elif quest.lower() == "decline":
                        print("You have declined the quest. You spend the rest of the evening with the tribe and you sleep there overnight.")    
                elif pathway2.lower() == "hide":
                    print("You jumped into nearby bush and poisonous snake bites you. Game Over")
        elif dragon.lower() == "wind":
            print("Dragon's ancestors used magic on dragon to protect them against wind magic, Draggon attacks you and you die")
    else:
        print("You jumped into the river and was eaten by crocodiles...RIP")
else:
    print("You chose the wrong path and you already failed your adventure...")