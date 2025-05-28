import random

# Gets the information of each player participating in the tournament, and enters them into the tournament.
def enterPlayers():
    playerList = []
    print("Please enter a minimum of four players for the tournament.")
    print("When you are done entering players, enter 'Exit'.")
    morePlayersNeeded = True
    addingPlayers = True
    while (addingPlayers):
        playerName = input("Please enter the name of player # " + str(len(playerList) + 1) + ": ")
        if (playerName.lower() == "exit" and len(playerList) > 3):
            addingPlayers = False
        elif (playerName.lower() == "exit"and len(playerList) < 4):
            print("Please make sure you have 4 players before you exit.")
        else:
            playerList.append(playerName)

    return playerList

# Adds extra players that were not added in the initial lineup.
def addExtraPlayers():
    addingPlayers = True
    while(addingPlayers):
        print("Current Player List:")
        print(playerList)
        playerName = input("Enter the name of the new player to be added: ")
        playerList.append(playerName)
        done = "x"
        while(done.lower() != "yes" and done.lower() != "no"):
            done = input("Are you done adding new players (Yes/No): ")
        if (done.lower() == "yes"):
            addingPlayers = False

# Removes any players that were in the initial lineup.
def removePlayers():
    removingPlayers = True
    while(removingPlayers):
        print("Current Player List:")
        print(playerList)
        playerName = input("Enter the name of the player to be removed: ")
        if (playerList.count(playerName) == 0):
            print("ERROR: Player not found on list, please try again.")
        elif (len(playerList) > 4):
            playerList.remove(playerName)
        else:
            print("Cannot remove any more players, as it would go beneath the required amount.")
        done = "x"
        while(done.lower() != "yes" and done.lower() != "no"):
            done = input("Are you done removing players (Yes/No): ")
        if (done.lower() == "yes"):
            removingPlayers = False

playerList = enterPlayers()
doneWithList = False
# Asks if the organizer wants/needs to remove any more players before the Tournament begins.
while(doneWithList == False):
    print("")
    print(playerList)
    print("Here is the current player list you have created. If you want to add more players, type ADD, if you want to remove more players, type REMOVE. Enter any other value to get started with the tournament.")
    playerChoice = input("Choice: ")   
    if (playerChoice.lower() == "add"):
        addExtraPlayers()
    elif (playerChoice.lower() == "remove"):
        removePlayers()
    else:
        doneWithList = True

swissRounds = 0
topCut = 0
topCutPlayers = 0
# Goes through the number of players and determines how large/if there is a top cut, and how many rounds of swiss there are.
# 4-7, 3 rounds of swiss, no top cut.
if (len(playerList) < 8):
    swissRounds = 3
    topCut = 0
# 8, 3 rounds of swiss, top cut of 2.
elif (len(playerList) == 8):
    swissRounds = 3
    topCut = 1
# 9-16, 4 rounds of swiss, top cut of 4.
elif (8 < len(playerList) <= 16):
    swissRounds = 4
    topCut = 2
# 17-32, 5 rounds of swiss, top cut of 8.
elif (17 <= len(playerList) <= 32):
    swissRounds = 5
    topCut = 3
# 33-64, 6 rounds of swiss, top cut of 8.
elif (33 <= len(playerList) <= 64):
    swissRounds = 6
    topCut = 3
# 65-128, 7 rounds of swiss, top cut of 8.
elif (65 <= len(playerList) <= 128):
    swissRounds = 7
    topCut = 3
# 129-226, 8 rounds of swiss, top cut of 8.
elif (129 <= len(playerList) <= 226):
    swissRounds = 8
    topCut = 3
# 227-256, 8 rounds of swiss, top cut of 16.
elif (227 <= len(playerList) <= 256):
    swissRounds = 8
    topCut = 4
# 257-409, 9 rounds of swiss, top cut of 16.
elif (257 <= len(playerList) <= 409):
    swissRounds = 9
    topCut = 4
# 410-512, 9 rounds of swiss, top cut of 32
elif (410 <= len(playerList) <= 512):
    swissRounds = 9
    topCut = 5
# 513+, 10 rounds of swiss, top cut of 32
elif (513 <= len(playerList)):
    swissRounds = 10
    topCut = 5

print()
if (topCut > 0):        
    print("There are " + str(len(playerList)) + " players in the tournament, so there will be " + str(swissRounds)  + " rounds of swiss into a top cut of " + str(2 ** topCut) + "!")
else:
    print("There are " + str(len(playerList)) + " players in the tournament, so there will be " + str(swissRounds)  + " rounds of swiss with no top cut!")

currentRound = 1

while (currentRound <= swissRounds):
    # Creates the matchups for the round:
    print("Round " + str(currentRound) + " matchups:")

    currentRound = currentRound + 1