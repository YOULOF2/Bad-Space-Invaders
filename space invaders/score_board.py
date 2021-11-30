from turtle import Turtle
from dataclasses import dataclass

FONT = ("Arial", 15, "bold")
SCOREBOARD_FONT = "#FFC0CB"


@dataclass()
class ScoreBoard:
    player_lives: int = 3
    player_score: int = 0


class DrawScoreBoard(Turtle):
    def __init__(self):
        super(DrawScoreBoard, self).__init__()
        self.pencolor(SCOREBOARD_FONT)
        self.penup()
        self.speed(0)
        self.hideturtle()

        self.screen = self.getscreen()

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.goto(-370, 360)
        self.write(f"Your Score: {scoreboard.player_score}", font=FONT)

        self.goto(-370, -370)
        self.write(f"Lives left: {scoreboard.player_lives}", font=FONT)
        self.screen.update()


scoreboard = ScoreBoard()
