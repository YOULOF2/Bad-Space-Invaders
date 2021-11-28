from turtle import Turtle

FONT = ("Arial", 12, "Bold")
SCOREBOARD_FONT = "#FFFFFF"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor(SCOREBOARD_FONT)

        self.player_lives: int = 3
        self.player_score: int = 0

    def draw_scoreboard(self):
        self.goto(-360, 360)
        self.write(f"Your Score: {self.player_score}", font=FONT)

        self.goto(-360, -360)
        self.write(f"Lives left: {self.player_lives}")
