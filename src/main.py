import sys
import pygame
import pygbag
import os
#import pyopengl
import pygame_menu
import numpy as np

SCREEN_X = 1280
SCREEN_Y = 720
SCREEN = None
MENU_X = 1000
MENU_Y = 700
RECTS = []
RUNNING = True
SIMULATE = False

MENU_THEME = pygame_menu.themes.Theme(
    title_background_color=(0,0,0), # Black
    border_color=(255,255,255),
    border_width=5,
    fps=30,
    title_close_button=True,
    title_close_button_background_color= (255,0,0), # Red
    title_font=pygame_menu.font.FONT_MUNRO,
    title_font_color= (255,255,255),
    title_font_size=40,

    widget_box_background_color = (128,128,128), # Grey
    widget_box_border_color=(30,0,0), # Light Red
    widget_box_border_width=2,
    widget_font=pygame_menu.font.FONT_MUNRO,
)

#Functions

def drawGrid():
    # Draw the grid lines only
    global SCREEN
    for x in range(0, SCREEN.get_width(), 100):
        pygame.draw.line(SCREEN, (0, 0, 60), (x, 0), (x, SCREEN.get_height()))
    for y in range(0, SCREEN.get_height(), 100):
        pygame.draw.line(SCREEN, (0, 0, 60), (0, y), (SCREEN.get_width(), y))

def drawRects():
    global SCREEN
    global RECTS

    #Clear old rectangles
    SCREEN.fill((0,0,0))
    drawGrid()

    for rectangle in RECTS:
        # (Surface, color [R,G,B,A], rect, width)
        pygame.draw.rect(SCREEN, (255, 255, 255), rectangle, width=0)
    pygame.display.flip()

def removeRect(pos):
    global SCREEN
    global RECTS

    for i in range(len(RECTS) - 1, -1, -1):
        if RECTS[i].collidepoint(pos):
            RECTS.pop(i)
            drawRects()

def displayMenu():
    global SCREEN
    global MENU_THEME

    SCREEN.fill((0, 0, 0))
    menu = pygame_menu.Menu('Display', MENU_X, MENU_Y, theme=MENU_THEME)
    menu.add.button('Back', settingsMenu)

    menu.mainloop(SCREEN)
    pygame.display.flip()
    return

def controlsMenu():
    SCREEN.fill((0, 0, 0))
    menu = pygame_menu.Menu('Controls', MENU_X, MENU_Y, theme=MENU_THEME)
    menu.add.label('Controls coming soon')
    menu.add.button('Back', settingsMenu)

    menu.mainloop(SCREEN)
    pygame.display.flip()
    return

def settingsMenu():
    global SCREEN
    global MENU_THEME

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
    global SCREEN
    global MENU_THEME
    global RUNNING

    SCREEN.fill((0, 0, 0))
    menu = pygame_menu.Menu('Options', MENU_X, MENU_Y, theme=MENU_THEME)
    menu.add.button('Resume', settingsMenu)
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
    global SCREEN
    global MENU_THEME

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
    global RECTS
    global SCREEN
    global RUNNING
    global SIMULATE

    SCREEN.fill((0, 0, 0))
    #Draw the grid
    drawGrid()
    pygame.display.flip()
    clock = pygame.time.Clock()
    
    RUNNING = True
    while RUNNING == True:
        clock.tick(30)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                return
        
        #Get mouse input
        mousePos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        mouseInput = pygame.mouse.get_pressed()
        #Get keyboard input
        keys = pygame.key.get_pressed()
        
        #Parse input
        if keys[pygame.K_ESCAPE]: # Open the options menu
            optionsMenu()
            if not RUNNING:
                break
        if keys[pygame.K_RETURN]:
            #Reverse if the simulation is running
            #NOTE: Doesn't always work as expected
            SIMULATE = not SIMULATE
        if not SIMULATE:
            if keys[pygame.K_c]:  # Clear screen when 'c' is pressed
                RECTS = []
                drawRects()
        
            if mouseInput[0]:  # Left mouse button make a white box
                #Snap position to grid
                x,y = mousePos
                
                if x % 10 != 0:
                    x -= x % 10
                if y % 10 != 0:
                    y -= y % 10
                #Draw rect at grid location
                newRect = pygame.Rect(x, y, 10, 10)

                if not any(rect.colliderect(newRect) for rect in RECTS):
                    RECTS.append(newRect)
                    drawRects()

            if mouseInput[2]:  # Right mouse button get rid of white box
                #Snap position to grid
                x,y = mousePos
                
                if x % 10 != 0:
                    x -= x % 10
                if y % 10 != 0:
                    y -= y % 10
                removeRect((x,y))

            prev_mouse = mouseInput
        if SIMULATE:
            #Game Simulation logic
            #Check Rectangles if they have neighbors
                #Get rectangle
                    #Get neighbors
                    #Check count                    
            #If more than 3 neighbors rectangle "lives"
            #Else rectangle "dies"

            pass
    return

def main():
    global SCREEN
    if sys.platform != "emscripten":
        import importlib
        importlib.import_module("pygame_menu")
        #importlib.import_module("pyopengl")
    #Initialization
    pygame.init()
    try:
        SCREEN = pygame.display.toggle_fullscreen()
        pygame.RESIZABLE
        pygame.SCALED
        
    except Exception as e:
        try:
            SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
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
