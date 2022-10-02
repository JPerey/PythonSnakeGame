# 1: create a snake body

# 2: How to move a snake

# 3: How to control the snake

# 4: detect collision with food

# 5: create a scoreboard

# 6: detect collision with wall

# 7: detect collision with tail

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes!")
screen.tracer(0)


# methods

def create_snake():
    snake = []
    snake_pos = 0
    snake_tick = 0
    for i in range(3):
        snake.append(Turtle())
        snake[i].shape("square")
        snake[i].color("white")
        snake[i].speed(10)
        snake[i].penup()
        snake[i].setx(snake_pos - (20 * snake_tick))
        snake_tick += 1

    return snake


# def turn_left(snake):
#     snake[0].left(90)


def game_run(snake):
    game_over = False

    while not game_over:
        screen.update()
        time.sleep(.2)
        for i in range(len(snake) -1, 0, -1):
            new_x = snake[i - 1].xcor()
            new_y = snake[i - 1].ycor()
            snake[i].goto(new_x, new_y)
        snake[0].forward(20)


starting_snake = create_snake()
game_run(starting_snake)

screen.exitonclick()
