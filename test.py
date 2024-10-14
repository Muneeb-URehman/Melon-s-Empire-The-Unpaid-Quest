from print import *

#starting of game;

#setting array for the screen
#screen is about 50 by 50 characters which will be changed later or improved

screenRow = 5
screenColumn = 5

screen = [['*' for i in range(screenRow)] for j in range(screenColumn)]

defScreen(screen, screenRow, screenColumn)

writeText(screen, screenRow, screenColumn, "x  y", 5/10, 3/10)


printScreen(screen, screenRow,screenColumn)

