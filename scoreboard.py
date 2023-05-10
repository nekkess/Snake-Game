from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scores.txt", mode="r") as file:
            contents = file.read()
            self.highscore = contents
        self.penup()
        self.goto(0, 200)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("scores.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     raphael = Turtle()
    #     raphael.color("white")
    #     raphael.hideturtle()
    #     raphael.write("GAME OVER.", move=False, align="center", font=("Courier", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore} ", move=False, align="center", font=("Courier", 16, "normal"))

    def incearse_score(self):
        self.score += 1
        self.update_scoreboard()
