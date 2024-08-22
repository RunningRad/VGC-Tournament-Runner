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
            done = input("Are you done adding new players (Yes/No): ")
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


