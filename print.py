def printScreen(screen,screenRow, screenColumn):

    for i in range(screenRow):
        for j in range(screenColumn):
            print(screen[i][j], end = ' ')
        print('')

def defScreen(screen, screenRow, screenColumn):

    x = '*'

    for i in range(screenRow):
        for j in range(screenColumn):
            if (i == 0 or i == screenRow - 1 ):
                screen[i][j] = '='
            elif (j == 0 or j == screenColumn - 1 ):
                screen[i][j] = '|'
            else:
                screen[i][j] = x

def writeText(screen, screenRow, screenColumn, text, percentLeft, percentTop):

    if (percentTop >= 1 or percentLeft >= 1 or percentLeft <= 0 or percentTop <= 0):
        print("error: use percentTop, percentLeft with range of 0 to 1")
        return

    # error checking for text longer than the screen
    if (len(text) > screenColumn - 2):
        print("error:  please increase the size of screen")
        return

    #checking row and columns for the writing
    row = int(percentTop * screenRow)
    column = int(percentLeft * screenColumn - len(text)//2)

    # adding text to the location
    for char in text:
        screen[row][column] = char
        column += 1