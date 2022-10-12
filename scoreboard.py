from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.check_high_score()
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score = {self.score} High Score: {self.high_score}", True, font=("Arial", 10, "normal"))

    def reset(self):
        archived_score = int(self.check_high_score())

        if self.score > archived_score:
            self.set_high_score()
        self.score = 0
        self.print_score()

    def set_high_score(self):
        self.high_score = self.score
        with open("score.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.print_score()

    def check_high_score(self):
        with open("score.txt") as file:
            archived_score = file.read()
        self.high_score = archived_score
        return archived_score


    def game_over(self):
        self.clear()
        self.goto(-30, 270)
        self.write(f"Final Score = {self.score} \nGAME OVER", True, font=("Arial", 10, "normal"))
