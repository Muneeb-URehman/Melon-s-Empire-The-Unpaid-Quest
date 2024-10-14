def printScreen(screen,screenRow, screenColumn):

    for i in range(screenRow):
        for j in range(screenColumn):
            print(screen[i][j], end = ' ')
        print('')

def defScreen(screen, screenRow, screenColumn):

    x = '*'

    for i in range(screenRow):
        for j in range(screenColumn):
            screen[i][j] = x

def writeText(screen, screenRow, screenColumn, text, percentLeft, percentTop):

    row = percent