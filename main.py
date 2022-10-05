# 1: create a snake body

# 2: How to move a snake

# 3: How to control the snake

# 4: detect collision with food

# 5: create a scoreboard

# 6: detect collision with wall

# 7: detect collision with tail

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
game_speed = .2
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes!")
screen.tracer(0)
snake = Snake()
screen.listen()

screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")


# methods


def game_run(game_speed):
    game_over = False

    while not game_over:
        screen.update()
        time.sleep(game_speed)
        snake.move()


game_run(game_speed)
screen.exitonclick()
