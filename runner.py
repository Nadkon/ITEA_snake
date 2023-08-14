import pygame as pg
import random
import time
from constants import *
from snake import Snake
from apple import Apple


pg.init()
running = True
pg.display.set_caption('Snake')

#rect = pg.Rect(100, 100, 100, 100)

apple = Apple(round(random.randrange(0, SCREEN_WIDTH, SQUARE_WIDTH)), round(random.randrange(0, SCREEN_HEIGHT, SQUARE_HIGHT)))
snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
font_style = pg.font.SysFont(None, 50)

snake_list = []
snake_lenght = 1
snake_head = []

if len(snake_list) > snake_lenght:
  del snake_list[0]

def message(msg,color):
   mesg = font_style.render(msg, True, color)
   SCREEN.blit(mesg, [SCREEN_WIDTH/2, SCREEN_HEIGHT/2])

def our_snake(width, snake_list):
        for x in snake_list:
            pg.draw.rect(SCREEN, 'green', [x[0], x[1], width, width])
our_snake(10, snake_list)
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
    if event.type == pg.KEYDOWN:

      if event.key == pg.K_UP:
        snake.move(pg.K_UP)
      if event.key == pg.K_DOWN:
        snake.move(pg.K_DOWN)
      if event.key == pg.K_RIGHT:
        snake.move(pg.K_RIGHT)
      if event.key == pg.K_LEFT:
        snake.move(pg.K_LEFT)

    SCREEN.fill('purple')

    apple.draw(SCREEN)
    #print(f"Apple: {apple.x}, {apple.y}")
    snake.draw(SCREEN)
    #print(f"Snake: {snake.x}, {snake.y}")
    if snake.x >= (SCREEN_WIDTH) or snake.x < 0 or snake.y >= (SCREEN_HEIGHT * 26) or snake.y < 0:
      message("GAME OVER :(",'red')
      running = False


    snake_head.append(snake.x)
    snake_head.append(snake.y)
    snake_list.append(snake_head)

    pg.display.update()

    if snake.x == apple.x and snake.y == apple.y:
      snake_lenght += 1
      apple = Apple(round(random.randrange(0, SCREEN_WIDTH, SQUARE_WIDTH)), round(random.randrange(0, SCREEN_HEIGHT, SQUARE_HIGHT)))
      #apple.draw(SCREEN)
      #pg.display.update()
    #pg.draw.rect(SCREEEN, 'red', (100, 50, WIDTH, HEIGHT))
    #pg.display.flip()

    CLOCK.tick(60)
time.sleep(2)
pg.quit()