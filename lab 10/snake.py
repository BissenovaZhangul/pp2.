import pygame, sys
import random, psycopg2
import time as t
pygame.init()



hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'zhangul_06'
port_id = 5432
conn, cur = None, None


con = psycopg2.connect(
      host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
)
cur = con.cursor()


cur.execute(
   '''CREATE TABLE IF NOT EXISTS usertable(
   username varchar(100),
   user_score int,
   user_level int
   )'''
)
con.commit()

W = 600
sec = 0
blocksize = 25
screen = pygame.display.set_mode((W, W))
caption = pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
fps = 12
lev = 0
SCORE = 0
LEVEL = 0
running = True
level_font = pygame.font.SysFont("Verdana", 30)
score_font = pygame.font.SysFont("Verdana", 30)
pause = False


time_event = pygame.USEREVENT
pygame.time.set_timer(time_event, 1000)


def insertname(username):
   cur.execute(
      "INSERT INTO usertable VALUES('{}', 0, 0)".format(username)
   )
   con.commit()

def upd(user):
   cur.execute(
      "SELECT * FROM usertable WHERE username = '{}'".format(user)
   )
   row = cur.fetchone()
   cur.execute(
      "UPDATE usertable SET user_score = '{}', user_level = '{}' WHERE username = '{}'".format 
      (max(row[1], SCORE), max(row[2], LEVEL), user)
   )
   con.commit()

print("Enter your name")
username = input()
cur.execute("SELECT count(*) FROM usertable WHERE username='{}'".format(username))
con.commit()
if cur.fetchone()[0] == 0:
   insertname(username)
   con.commit()
else:
      cur.execute("SELECT * FROM usertable WHERE username = '{}'".format(username))
      data=cur.fetchone()
      print("User's max score:{}".format(data[1]))
      print("User's max level:{}".format(data[2]))


class GoldApple:
   def __init__(self):
      self.x = int(random.randint(0, W)/ blocksize) * blocksize
      self.y = int(random.randint(0, W)/ blocksize) * blocksize
      self.rect = pygame.Rect(self.x, self.y, blocksize, blocksize)
   def update(self):
      pygame.draw.rect(screen, 'yellow', self.rect)
# food
class Apple:
   def __init__(self):
      self.x = int(random.randint(0, W)/ blocksize) * blocksize
      self.y = int(random.randint(0, W)/ blocksize) * blocksize
      self.rect = pygame.Rect(self.x, self.y, blocksize, blocksize)
   
   def update(self):
      pygame.draw.rect(screen, 'red', self.rect)

# snake
class Snake:
   def __init__(self):
      self.x, self.y = blocksize, blocksize
      self.xdir, self.ydir = 1, 0
      self.body = [pygame.Rect(self.x, self.y, blocksize, blocksize)]
      self.head = self.body[0]
      self.dead = False
   def update(self):
      global apple
      global LEVEL
      global SCORE
      global fps
      # collision
      for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
                upd(username)
            if self.head.x not in range(0, W) or self.head.y not in range(0, W):
                self.dead = True
                upd(username)
      # restart
      if self.dead:
            fps = 12
            self.x, self.y = blocksize, blocksize
            self.head = pygame.Rect(self.x, self.y, blocksize, blocksize)
            self.body = [pygame.Rect(self.x, self.y, blocksize, blocksize)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            SCORE = 0
            LEVEL = 0
      # move
      self.body.append(self.head)
      for i in range(len(self.body) - 1):
         self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
      self.head.x += self.xdir * blocksize
      self.head.y += self.ydir * blocksize 
      self.body.remove(self.head)
flag = True
# setka
def drawgrid():
   for x in range(0, W, blocksize):
      for y in range(0, W, blocksize):
         rect = pygame.Rect(x, y, blocksize, blocksize)
         pygame.draw.rect(screen, (255, 255, 255), rect, 1)
apple = Apple()
snake = Snake()
goldapple = GoldApple()
# game loop
while running:
   for event in pygame.event.get():
      if event.type == time_event:
         sec += 1
      if event.type == pygame.QUIT:
         running = False
         cur.close()
         con.close()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            snake.xdir, snake.ydir = 0, -1
         elif event.key == pygame.K_DOWN:
            snake.xdir, snake.ydir = 0, 1
         elif event.key == pygame.K_LEFT:
            snake.xdir, snake.ydir = -1, 0
         elif event.key == pygame.K_RIGHT:
            snake.xdir, snake.ydir = 1, 0
         if event.key == pygame.K_SPACE:
            upd(username)
            pause = True
   while pause:   
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            cur.close()
            con.close()
            sys.exit()
         if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
            pause = False
      unpause = level_font.render('Press u to unpause', True, 'white')
      screen.blit(unpause, unpause.get_rect(center = (W // 2, W // 2)))
      pygame.display.update()

   if sec > 5:
      apple = Apple()
      sec = 0

   snake.update()
   screen.fill('black')
   
   score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 255))
   screen.blit(score, (0, 0))
   level = level_font.render(f"Your level: {LEVEL}", True, (0, 0, 255))
   screen.blit(level, (W - 200, 0))
   if flag:
      apple.update()
   if flag == False:
      goldapple.update()

   pygame.draw.rect(screen, 'green', snake.head)

   for body in snake.body:
      pygame.draw.rect(screen, 'green', body)
   # eating 
   if snake.head.x == apple.x and snake.head.y == apple.y:
      sec = 0
      snake.body.append(pygame.Rect(body.x, body.y,blocksize, blocksize))
      rand = int(random.randint(0, 4))
      if rand == 0:
         flag = False
         goldapple = GoldApple()
      else:
         flag = True
         apple = Apple()
      SCORE += 1
      if SCORE % 2 == 0:
         fps += 1
         LEVEL += 1
   #eating goldapple
   if snake.head.x == goldapple.x and snake.head.y == goldapple.y:
      sec = 0
      for i in range(4):
         snake.body.append(pygame.Rect(body.x, body.y,blocksize, blocksize))
      SCORE += 4
      rand = int(random.randint(0, 4))
      if rand == 0:
         flag = False
         goldapple = GoldApple()
      else:
         flag = True
         apple = Apple()
      
      fps += 2
      LEVEL += 2
   
   
   clock.tick(fps)
   pygame.display.update()

            
   