def createMenu(listOfChoices,menuTitle):  #Takes a list of choices and its title and return a menu
    tmpString = menuTitle + "\n"
    ct = 0
    for item in listOfChoices:
        ct += 1
        tmpString += str(ct)+"."+ item
        tmpString += "\n"
    return tmpString  
