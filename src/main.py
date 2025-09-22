import pygame

# Initializations
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
rectPos = []
remPos = []

#Game begins
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black
    pygame.display.flip()  # Update the display
    #clock.tick(60)  # Maintain 60 FPS
    #Intro Screen

    #Clear screen
    screen.fill((0, 0, 0))
    pygame.display.flip()

    #Draw grid
    for x in range(0, 1920, 100):
        pygame.draw.line(screen, (0, 0, 60), (x, 0), (x, 1080))
    
    #Get mouse input
    mouseX = pygame.mouse.get_pos()[0] - 10
    mouseY = pygame.mouse.get_pos()[1] - 10
    mouseInput = pygame.mouse.get_pressed()

    if mouseInput[0]:  # Left mouse button make a white box
        #store the position for to draw the rectangles
        rectPos.append([mouseX, mouseY])

    if mouseInput[2]:  # Right mouse button get rid of white box
        #store the position to remove rectangles
        remPos.append([mouseX, mouseY])

    #Get keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_c]:  # Clear screen when 'c' is pressed
        screen.fill((0, 0, 0))
    if keys[pygame.K_s]: # Move screen down when 's' is pressed
        screen.scroll(dy=100)
    if keys[pygame.K_w]: # Move screen up when 'w' is pressed
        screen.scroll(dy=-100)
    if keys[pygame.K_a]: # Move screen left when 'a' is pressed
        screen.scroll(dx=-100)
    if keys[pygame.K_d]: # Move screen right when 'd' is pressed
        screen.scroll(dx=100)()
    
    #Drawing / Removing
    if len(rectPos) > 1:
        #Draw rectangles
        i = 0
        while i < len(rectPos):
            pygame.draw.rect(screen, (255, 255, 255), (rectPos[i][0], rectPos[i][1], 10, 10), width = 0)
            i += 1

    if len(remPos) > 1:
        #remove the rect
        #Check rectPos for a matching x,y
        i = 0
        while i < len(rectPos):
            posx = rectPos[i][0]
            remx = remPos[0][0]
            up = True
            #if match
            if remx == posx:
                #remove the rectangle
                pygame.draw.rect(screen, (0, 0, 0), (rectPos[i][0], rectPos[i][1], 10, 10), width = 0)
                #Delete both entries
                rectPos.remove(i)
                remPos.pop()
            if remPos[0][0] != posx:
                if up == True:
                    remx += 1
                if up == False:
                    remx -= 1
                #Check if difference is greater than 10
                if (remx - remPos[0][0]) > 10 or (remx - remPos[0][0]) < -10:
                    if up == True:
                        #Skip area already searched
                        remx - 10
                    if up == False:
                        #Skip area already searched
                        remx + 10
                    up = not(up)
    
    #Game Logic

        
    #Update screen
    pygame.display.flip()