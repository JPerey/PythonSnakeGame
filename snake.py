from turtle import Turtle

STARTING_POSITIONS = ((-10,0), (-30,0), (-50,0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.degrees(360)
            new_segment.speed(5)
            new_segment.penup()
            new_segment.goto(i)
            self.snake_segments.append(new_segment)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def increase_size(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.degrees(360)
        new_segment.speed(5)
        new_segment.penup()
        new_segment.goto(self.snake_segments[-1].xcor() - 10, self.snake_segments[-1].ycor() - 10)
        self.snake_segments.append(new_segment)


    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.seth(RIGHT)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.seth(270)

