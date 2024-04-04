import pygame as pg 
from datetime import datetime as dt

pg.init()
screen = pg.display.set_mode((800, 800))
window_title = pg.display.set_caption("mickey mouse clock")

clock = pg.time.Clock()

bg_surf = pg.image.load(r"images/mainclock.png")
leftarm_surf = pg.image.load(r"images/leftarm.png")
rightarm_surf = pg.image.load(r"images/rightarm.png")
bg_rect = bg_surf.get_rect(center = (400, 400))

done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    current_time = dt.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pg.transform.rotate(leftarm_surf, seconds_angle)
    rotated_rightarm = pg.transform.rotate(rightarm_surf, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center = bg_rect.center)
    rightarm_rect = rotated_rightarm.get_rect(center = bg_rect.center)

    screen.blit(bg_surf, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pg.display.flip()
    clock.tick(60)