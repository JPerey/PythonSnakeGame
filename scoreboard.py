from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.print_score(new_score=0)

    def print_score(self, new_score):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score = {new_score}", True, font=("Arial", 10, "normal"))


    def game_over(self, new_score):
        self.clear()
        self.goto(-30, 270)
        self.write(f"Final Score = {new_score} \nGAME OVER", True, font=("Arial", 10, "normal"))