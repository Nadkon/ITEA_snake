import pygame as pg
import random
from constants import *
from snake import Snake
from apple import Apple


pg.init()
running = True
pg.display.set_caption('Snake')

rect = pg.Rect(100, 100, 100, 100)

snake = Snake(WIDTH * 15, HEIGHT * 13)
apple = Apple(round(random.randrange(WIDTH * 30)), round(random.randrange(HEIGHT * 26)))


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

    SCREEEN.fill('purple')

    snake.draw(SCREEEN)
    apple.draw(SCREEEN)
    #pg.draw.rect(SCREEEN, 'red', (100, 50, WIDTH, HEIGHT))
    #pg.display.flip()
    pg.display.update()

    CLOCK.tick(60)

pg.quit()