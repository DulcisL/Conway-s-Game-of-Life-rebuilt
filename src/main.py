import pygame

#Functions
def drawRects(rects):
    for rectangle in rects:
                            #(Surface, color [A], rect, width)
        pygame.draw.rect(screen, (255, 255, 255, 1), rectangle, width=0)
        #update screen
        pygame.display.update(rectangle)
        print(f"I have displayed the rectangle")
        return 1

def removeRect(rects, pos):
    print(f"I am removing rectangle at {pos}")
    for rectangle in rects:
        if rectangle.collidepoint(pos):
            rects.remove(rectangle)
            print(f"I have removed the rectangle")
            #update screen
            pygame.display.update(rectangle)
            return 1
        return 0


# Initializations
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
rects = []

screen.fill((0, 0, 0))  # Clear screen with black

#Game begins
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()  # Update the display
    clock.tick(30)  # Maintain 30 FPS
    #Intro Screen

    #Clear screen
    pygame.display.flip()

    #Draw grid
    for x in range(0, screen.get_width(), 100):
                        #(surface, color, start_pos, end_pos)
        pygame.draw.line(screen, (0, 0, 60), (x, 0), (x, screen.get_width()))
    for y in range (0, screen.get_height(), 100):
        pygame.draw.line(screen, (0, 0, 60), (0, y), (screen.get_width(), y))
    
    #Get mouse input
    mousePos = (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1] - 10)
    mouseInput = pygame.mouse.get_pressed()

    if mouseInput[0]:  # Left mouse button make a white box
        #Snap position to grid
        x,y = mousePos
        if x % 10 == 0 and y % 10 == 0:
            break
        if x % 10 != 0:
            x += 10 - (x % 10)
        if y % 10 != 0:
            y += 10 - (y % 10)
        #Draw rect at grid location
        newRect = pygame.Rect(x, y, 10, 10)
        if len(rects) == 0:
            rects.append(newRect)
        if len(rects) != 0:
            for rectangle in rects:
                if rectangle.colliderect(newRect) == False:
                    rects.append(newRect)

        drawRects(rects)
            

    if mouseInput[2]:  # Right mouse button get rid of white box
        #remove rect
        removeRect(rects, mousePos)

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
    
    #Game Logic

        
    #Update screen
    pygame.display.flip()