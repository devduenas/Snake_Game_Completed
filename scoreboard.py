from turtle import Turtle
ALIGNMENT = "center"
FONT_SPECS = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT_SPECS)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT_SPECS)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
