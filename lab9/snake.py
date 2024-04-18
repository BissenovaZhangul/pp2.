import pygame
import time
import random

pygame.init()

dis = pygame.display.set_mode((800, 600))
dis_width = 800
dis_height = 600
pygame.display.set_caption("SNAKE")

BLUE = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

snake = 10
speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("timesnewroman", 50)
score_font = pygame.font.SysFont("comicsansms", 35)

def thesnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])

def text_end(text, color):
    mesg = font_style.render(text, True, color)
    dis.blit(mesg, [275, 290])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, PURPLE)
    dis.blit(value, [0, 0])

def main():
    game_over = False
    game_close = False
    score = 0
    x = dis_width / 2
    y = dis_height / 2

    snake_list = []
    snake_length = 1

    food_timer = 100  # Timer for food disappearance
    food_spawned = False
    foodx = 0
    foody = 0
    new_x = 0
    new_y = 0

    while not game_over:
        while game_close:
            dis.fill(WHITE)
            text_end("GAME OVER", RED)
            Your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
             
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    new_x = snake
                    new_y = 0
                elif event.key == pygame.K_LEFT:
                    new_x = -snake
                    new_y = 0
                elif event.key == pygame.K_DOWN:
                    new_x = 0
                    new_y = snake
                elif event.key == pygame.K_UP:
                    new_x = 0
                    new_y = -snake

        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True

        x += new_x
        y += new_y
        dis.fill(WHITE)

        # Check if food is spawned and decrement timer
        if food_spawned:
            food_timer -= 1

        # If timer reaches 0, reset timer and spawn new food
        if food_timer == 0:
            food_spawned = False
            food_timer = 100

        # If food is not spawned, generate new food
        if not food_spawned:
            foodx = round(random.randrange(0, dis_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake) / 10.0) * 10.0
            food_spawned = True

        pygame.draw.rect(dis, RED, [foodx, foody, snake, snake])

        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for q in snake_list[:-1]:
            if q == snake_Head:
                game_close = True
        thesnake(snake, snake_list)
        Your_score(snake_length - 1)

        pygame.display.update()

        # If snake eats food, increase score and length of snake
        if x == foodx and y == foody:
            snake_length += 1
            food_spawned = False

        clock.tick(speed)

    pygame.quit()
    quit()

main()
