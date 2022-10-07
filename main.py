# 1: create a snake body

# 2: How to move a snake

# 3: How to control the snake

# 4: detect collision with food

# 5: create a scoreboard

# 6: detect collision with wall

# 7: detect collision with tail

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
game_speed = .2
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes!")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")


# methods


def game_run(game_speed):
    game_over = False
    new_score = 0

    while not game_over:
        screen.update()
        time.sleep(game_speed)
        snake.move()

        #detect collision with food

        if snake.head.distance(food) < 15:
            food.move_food()
            new_score += 1
            snake.increase_size()
            scoreboard.print_score(new_score)

        #detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_over = True
            scoreboard.game_over(new_score)

        #detect collision with tail

        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                # PRINT
                print(snake.head.distance(segment))
                game_over = True
                scoreboard.game_over(new_score)



game_run(game_speed)
screen.exitonclick()
