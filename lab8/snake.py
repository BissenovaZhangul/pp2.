import pygame
import random

pygame.init()

FPS = 10
clock = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 105)

# Screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
STYLE_FONT = pygame.font.SysFont("bahnschrift", 25)

# Snake
SNAKE_BLOCK_SIZE= 15
SNAKE_SPEED = 1
X_POS = SCREEN_WIDTH // 2
Y_POS = SCREEN_HEIGHT // 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SNAKE")
pygame.display.update()


def Your_score(score):
    value = STYLE_FONT.render("SCORE: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])


def snake(SNAKE_BLOCK_SIZE, snake_list_len):
    for segment in snake_list_len:
        pygame.draw.rect(screen, YELLOW, [segment[0] - 3, segment[1] - 3, SNAKE_BLOCK_SIZE + 6, SNAKE_BLOCK_SIZE + 6])
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])


def mainLoop():
    running = True
    x = X_POS - SNAKE_BLOCK_SIZE // 2
    y = Y_POS - SNAKE_BLOCK_SIZE // 2
    x_change = 0
    y_change = 0
    snake_list_count = []
    len_snake = 1
    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE * 2))
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE * 2))
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK_SIZE
                    x_change = 0

        if x >= SCREEN_WIDTH + SNAKE_BLOCK_SIZE or x < 0 or y >= SCREEN_HEIGHT + SNAKE_BLOCK_SIZE or y < 0:
            running = False

        x += x_change
        y += y_change

        snake_head_rect = pygame.Rect(x, y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE)
        food_rect = pygame.Rect(food_x, food_y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE)

        if snake_head_rect.colliderect(food_rect):
            food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE * 2))
            food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE * 2))
            len_snake += 1
            
        for segment in snake_list_count[:-1]:
            if snake_head_rect.colliderect(pygame.Rect(segment[0], segment[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE)):
                running = False
                break

        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, [food_x, food_y], 5)
        snake_head = [x, y]
        snake_list_count.append(snake_head)
        if len(snake_list_count) > len_snake:
            del snake_list_count[0]
        snake(SNAKE_BLOCK_SIZE, snake_list_count)
        Your_score(len_snake - 1)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

mainLoop()