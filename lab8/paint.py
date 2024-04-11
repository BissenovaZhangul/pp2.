import pygame

def rectangle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    a = abs(x1-x2)
    b = abs(y1-y2)
    pygame.draw.rect(surf, color, (min(x1, x2), min(y1, y2), a, b), d)

def pen(surf, cur, end, d, color):
    pygame.draw.line(surf, color, cur, end, d)
    
def circle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = abs(x1-x2)
    b = abs(y1-y2)
    pygame.draw.circle(surf, color, (min(x1,x2)+a/2, min(y1, y2)+b/2), min(a, b)/2, d)

def eraser(surf, cur):
    x1, y1 = cur[0], cur[1]
    pygame.draw.circle(surf, "Black", (x1, y1), 20)

FPS = 60
W = 640
H = 480

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Paint')
baseLayer = pygame.Surface((640, 480))
clock = pygame.time.Clock()

mode = "Rectangle"
color = "Red"
isMouseDown = False
currentX = -1
currentY = -1
prevX = -1
prevY = -1


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = "Red"
            if event.key == pygame.K_b:
                color = "Blue"
            if event.key == pygame.K_g:
                color = "Green"
            if event.key == pygame.K_w:
                color = "White"
            
            if event.key == pygame.K_1:
                mode = "Rectangle"
            if event.key == pygame.K_2:
                mode = "Circle"
            if event.key == pygame.K_3:
                mode = "Pen"
            if event.key == pygame.K_4:
                mode = "Eraser"

        if event.type == pygame.MOUSEBUTTONDOWN:
            xnow = event.pos[0]
            ynow = event.pos[1]
            last_pos = (xnow, ynow)
            isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            isMouseDown = False
            baseLayer.blit(screen, (0,0))
       
        if event.type == pygame.MOUSEMOTION:
            if isMouseDown == True:
                if mode == 'Pen':
                    pen(baseLayer, last_pos, (xnow, ynow), 1, color)
                    last_pos = (xnow, ynow)
                xnow = event.pos[0]
                ynow = event.pos[1]

    if isMouseDown == True and last_pos[0] != -1 and last_pos[1] != -1 and xnow != -1 and ynow != -1:
        screen.blit(baseLayer, (0, 0))
        if mode == 'Rectangle':
            rectangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Circle':
            circle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == "Eraser":
            eraser(baseLayer, (xnow, ynow))

    pygame.display.update()
    clock.tick(144)