import pygame

def draw_rectangle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    a = abs(x1-x2)
    b = abs(y1-y2)
    pygame.draw.rect(surf, color, (min(x1, x2), min(y1, y2), a, b), d)

def draw_pen(surf, cur, end, d, color):
    pygame.draw.line(surf, color, cur, end, d)
    
def draw_circle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = abs(x1-x2)
    b = abs(y1-y2)
    pygame.draw.circle(surf, color, (min(x1,x2)+a/2, min(y1, y2)+b/2), min(a, b)/2, d)

def draw_eraser(surf, cur):
    x1, y1 = cur[0], cur[1]
    pygame.draw.circle(surf, "Black", (x1, y1), 20)

def draw_square(surf, cur, end, d, color):
    x, y, x_end, y_end = cur[0], cur[1], end[0], end[1]
    side = max(abs(x_end - x), abs(y_end - y))
    draw_rectangle(surf, (x, y), (x + side, y + side), d, color)

def draw_right_triangle(surf, cur, end, d, color):
    x, y = cur[0], cur[1]
    x_end, y_end = end[0], end[1]
    pygame.draw.polygon(surf, color, [(x, y), (x, y_end), (x_end, y_end)], d)

def draw_equilateral_triangle(surf, cur, end, d, color):
    x, y = cur[0], cur[1]
    x_end, y_end = end[0], end[1]
    cx = (x + x_end) / 2
    h = abs(y_end - y) * 0.866  # Height of an equilateral triangle
    pygame.draw.polygon(surf, color, [(x, y_end), (x_end, y_end), (cx, y)], d)

def draw_rhombus(surf, cur, end, d, color):
    x, y = cur[0], cur[1]
    x_end, y_end = end[0], end[1]
    cx = (x + x_end) / 2
    cy = (y + y_end) / 2
    pygame.draw.polygon(surf, color, [(cx, y), (x_end, cy), (cx, y_end), (x, cy)], d)

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
            if event.key == pygame.K_5:
                mode = "Square"
            if event.key == pygame.K_6:
                mode = "Right Triangle"
            if event.key == pygame.K_7:
                mode = "Equilateral Triangle"
            if event.key == pygame.K_8:
                mode = "Rhombus"
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            xnow = event.pos[0]
            ynow = event.pos[1]
            last_pos = (xnow, ynow)
            isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            isMouseDown = False
            baseLayer.blit(screen, (0, 0))

        if event.type == pygame.MOUSEMOTION:
            if isMouseDown == True:
                if mode == 'Pen':
                    draw_pen(baseLayer, last_pos, (xnow, ynow), 1, color)
                    last_pos = (xnow, ynow)
                xnow = event.pos[0]
                ynow = event.pos[1]

    if isMouseDown == True and last_pos[0] != -1 and last_pos[1] != -1 and xnow != -1 and ynow != -1:
        screen.blit(baseLayer, (0, 0))
        if mode == 'Rectangle':
            draw_rectangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Circle':
            draw_circle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == "Eraser":
            draw_eraser(baseLayer, (xnow, ynow))
        elif mode == "Square":
            draw_square(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == "Right Triangle":
            draw_right_triangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == "Equilateral Triangle":
            draw_equilateral_triangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == "Rhombus":
            draw_rhombus(screen, last_pos, (xnow, ynow), 1, color)

    pygame.display.update()
    clock.tick(144)  