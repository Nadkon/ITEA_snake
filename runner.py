import pygame as pg
import random
from constants import *
from snake import Snake
from apple import Apple


pg.init()
running = True
pg.display.set_caption('Snake')

#rect = pg.Rect(100, 100, 100, 100)

apple = Apple(round(random.randrange(0, SCREEN_WIDTH, SQUARE_WIDTH)), round(random.randrange(0, SCREEN_HEIGHT, SQUARE_HIGHT)))
snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


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
      running = False
    if snake.x == apple.x and snake.y == apple.y:
      print('catch')
      apple = Apple(round(random.randrange(0, SCREEN_WIDTH, SQUARE_WIDTH)), round(random.randrange(0, SCREEN_HEIGHT, SQUARE_HIGHT)))
      apple.draw(SCREEN)
    #pg.draw.rect(SCREEEN, 'red', (100, 50, WIDTH, HEIGHT))
    #pg.display.flip()
    pg.display.update()

    CLOCK.tick(60)

pg.quit()