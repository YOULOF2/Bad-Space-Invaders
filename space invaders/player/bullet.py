from turtle import Turtle
from time import sleep
from datetime import datetime

SPEED = 10

MOVE_DISTANCE = 20

SLEEP_TIME = 0.009


class Bullet(Turtle):
    def __init__(self, start_coord: list, screen_obj):
        super().__init__()

        self.setheading(90)
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("white")
        self.penup()

        self.start_coord = start_coord
        self.goto(self.start_coord[0], self.start_coord[1])

        self.screen = screen_obj

    def move(self):
        self.showturtle()
        for _ in range(50):
            sleep(SLEEP_TIME)
            self.forward(MOVE_DISTANCE)
            self.screen.update()
