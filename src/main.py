import sys
import pygame
import os
import pygame_menu
import numpy as np
import math
import random as rand

SCREEN_X = 1920
SCREEN_Y = 1080
SCREEN = None
MENU_X = 1
MENU_Y = 1
CELL_SIZE = 10
RUNNING = True
SIMULATE = False
GRID_H = SCREEN_Y // CELL_SIZE
GRID_W = SCREEN_X // CELL_SIZE
GRID = np.zeros((GRID_H, GRID_W), dtype=bool)


MENU_THEME = pygame_menu.themes.Theme(
    title_background_color=(0,0,0), # Black
    border_color=(255,255,255),
    border_width=5,
    fps=30,
    title_close_button=True,
    title_close_button_background_color= (255,0,0), # Red
    title_font=pygame_menu.font.FONT_MUNRO,
    title_font_color= (255,255,255),
    title_font_size= 40,


    widget_box_background_color = (128,128,128), # Grey
    widget_box_border_color=(30,0,0), # Light Red
    widget_box_border_width=2,
    widget_font=pygame_menu.font.FONT_MUNRO,
)

#Functions

def updateGame():
    for x in range(GRID_W):
        for y in range(GRID_H):
            color = ()
            if GRID[y,x] == True:
                color = (255,255,255)
            if GRID[y,x] == False:
                color = (0,0,0)
            drawRect(x * CELL_SIZE, y * CELL_SIZE, color)
            
    drawGrid()
    pygame.display.flip()

def drawRect(x,y, color):
    #Draw the rectangle
    square = pygame.Rect((x,y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(SCREEN, color, square)

def drawGrid():
    # Draw the grid lines
    gridOffset = CELL_SIZE * 10
    for x in range(0, SCREEN.get_width(), gridOffset):
                       #(display,color, start, end)
        pygame.draw.line(SCREEN, (0, 0, 60), (x, 0), (x, SCREEN.get_height()))
    for y in range(0, SCREEN.get_height(), gridOffset):
        pygame.draw.line(SCREEN, (0, 0, 60), (0, y), (SCREEN.get_width(), y))

def displayMenu():

    SCREEN.fill((0, 0, 0))
    menu = pygame_menu.Menu('Display', MENU_X, MENU_Y, theme=MENU_THEME)
    menu.add.button('Back', settingsMenu)

    menu.mainloop(SCREEN)
    pygame.display.flip()
    return

def controlsMenu():
    SCREEN.fill((0, 0, 0))
    menu = pygame_menu.Menu('Controls', MENU_X, MENU_Y, theme=MENU_THEME)
    menu.add.label('Esc - Goes to the settings / options menu')
    menu.add.label('C - Clears the screen while in the game')
    menu.add.label('Left mouse - Adds a cell to the screen while in the game')
    menu.add.label('Right mouse - Removes a cell from the screen while in the game')
    menu.add.button('Back', settingsMenu)

    menu.mainloop(SCREEN)
    pygame.display.flip()
    return

def settingsMenu():

    SCREEN.fill((0, 0, 0))
    menu = pygame_menu.Menu('Display', MENU_X, MENU_Y, theme=MENU_THEME)

    menu.add.button('Display', displayMenu)
    menu.add.range_slider('Sound', default=100, range_values=(0,100), increment=1)
    menu.add.button('Controls', controlsMenu)
    menu.add.button('Main Menu', mainMenu)
    menu.add.button('Quit to Desktop', pygame_menu.events.EXIT)

    menu.mainloop(SCREEN)
    pygame.display.flip()
    return

def optionsMenu():
    global RUNNING

    SCREEN.fill((0, 0, 0))
    menu = pygame_menu.Menu('Options', MENU_X, MENU_Y, theme=MENU_THEME)
    menu.add.button('Resume', game)
    menu.add.button('Settings', settingsMenu)
    menu.add.button('Controls', controlsMenu)
    def quit_to_menu():
        global RUNNING
        RUNNING = False
        menu.disable()
    menu.add.button('Quit to Menu', quit_to_menu)
    menu.add.button('Quit to Desktop', pygame_menu.events.EXIT)

    menu.mainloop(SCREEN)
    pygame.display.flip()
    return

def mainMenu():
    # NOTE: For some reason mouse must click on item 2x on program start

    SCREEN.fill((0, 0, 0))
    mainTheme = MENU_THEME.copy()
    mainTheme.title_close_button=False
    menu = pygame_menu.Menu("Welcome to a python recreation of Conways's game of Life", MENU_X, MENU_Y, theme=mainTheme)

    menu.add.button('Play', game)
    menu.add.button('Settings', settingsMenu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)
    pygame.display.flip()
    return

def game():
    global SCREEN
    global RUNNING
    global SIMULATE
    global CELL_SIZE
    global GRID
    white = (255, 255, 255)
    black = (0, 0, 0)
    nlimit = 3


    SCREEN.fill(black)
    #Draw the grid
    drawGrid()
    pygame.display.flip()
    clock = pygame.time.Clock()
    
    RUNNING = True
    while RUNNING:
        if not SIMULATE:
            clock.tick(120)
        if SIMULATE:
            clock.tick(10)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    SIMULATE = not SIMULATE
                if event.key == pygame.K_c and not SIMULATE:
                    GRID[:] = False
                    SCREEN.fill(black)
                    drawGrid()
                if event.key == pygame.K_ESCAPE:
                    SIMULATE = False
                    optionsMenu()
        
        #Get mouse input
        mx, my = pygame.mouse.get_pos()
        #Snap to grid
        gx = mx // CELL_SIZE
        gy = my // CELL_SIZE

        if 0 <= gx < GRID_W and 0 <= gy < GRID_H:

            mouseInput = pygame.mouse.get_pressed()
            if not SIMULATE:

                if mouseInput[0]:  # Left mouse button make a white box
                    GRID[gy,gx] = True
                    drawRect(gx * CELL_SIZE, gy * CELL_SIZE, white)

                if mouseInput[2]:  # Right mouse button get rid of white box
                    GRID[gy,gx] = False
                    drawRect(gx * CELL_SIZE, gy * CELL_SIZE, black)

            if SIMULATE:
                #Game Simulation logic

                #Check neighbors
                NEXT = GRID.copy()
                for x in range(GRID_W):
                    for y in range(GRID_H):
                        neighbors = 0
                        for dx in (-1, 0, 1):
                            for dy in (-1, 0, 1):
                                if dx == 0 and dy == 0:
                                    continue
                                ny = (y + dy) % GRID_H
                                nx = (x + dx) % GRID_W
                                neighbors += GRID[ny,nx]

                        #Apply rules
                        #If nlimit neighbors persist if alive
                        if neighbors == nlimit - 1 and GRID[y,x]:
                            NEXT[y,x] = True

                        #if nlimit neighbors lives if dead (repop)
                        if neighbors == nlimit and not GRID[y,x]:
                            NEXT[y,x] = True

                        #if nlimit neighbors randomly lives or dies if alive (repop / overpop)
                        if neighbors == nlimit and GRID[y,x]:
                            rx = (x + rand.randint(-1,1)) % GRID_W
                            ry = (y + rand.randint(-1,1)) % GRID_H
                            NEXT[ry,rx] = rand.randint(0, 1)
                        
                        #if >nlimit dies (overpop)
                        if neighbors > nlimit or neighbors < (nlimit - 1):
                            NEXT[y,x] = False
                            
                GRID[:] = NEXT
        updateGame()
        if not RUNNING:
            return

def main():
    global SCREEN
    global SCREEN_X
    global SCREEN_Y
    global MENU_X
    global MENU_Y

    if sys.platform != "emscripten":
        import importlib
        importlib.import_module("pygame_menu")
    #Initialization
    pygame.init()
    try:
        #initialize the screen and set the height and widths
        SCREEN = pygame.display.set_mode((SCREEN_X,SCREEN_Y), pygame.RESIZABLE | pygame.SCALED)
        SCREEN_X, SCREEN_Y = SCREEN.get_size()

        MENU_Y = .9 * SCREEN_Y
        MENU_X = .8 * SCREEN_X

        ratio = (MENU_Y / MENU_X)

        #Set the correct Scale for menus
        MENU_THEME.title_font_size= min(50, math.floor(100 * ratio)) | max(50, math.floor(100 * ratio))
        MENU_THEME.widget_font_size= min(25, math.floor(50 * ratio)) | max(25, math.floor(100 * ratio))
        
    except Exception as e:
        print(e)
    finally:

        #Update screen
        pygame.display.flip()
        if(RUNNING == True):
            #Load menu
            mainMenu()
        if(RUNNING == False):
            pygame_menu.events.EXIT

if __name__=="__main__":
    main()
