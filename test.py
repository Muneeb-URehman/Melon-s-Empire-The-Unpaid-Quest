from print import *

#starting of game;

#setting array for the screen
#screen is about 50 by 50 characters which will be changed later or improved

screenRow = 20
screenColumn = 20

screen = [['*' for i in range(screenRow)] for j in range(screenColumn)]

defScreen(screen, screenRow, screenColumn)

writeText(screen, screenRow, screenColumn, "ColDol", 0.5, 0.3)

printScreen(screen, screenRow,screenColumn)