from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}    High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
