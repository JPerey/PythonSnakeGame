from turtle import Turtle

STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.degrees(360)
            new_segment.speed(10)
            new_segment.penup()
            new_segment.goto(i)
            self.snake_segments.append(new_segment)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segments[0].heading != -0:
            self.snake_segments[0].seth(90)

    def left(self):
        if self.snake_segments[0].heading != 180:
            self.snake_segments[0].seth(180)

    def right(self):
        if self.snake_segments[0].heading != 0:
            self.snake_segments[0].seth(0)

    def down(self):
        if self.snake_segments[0].heading != 270:
            self.snake_segments[0].seth(270)
