from turtle import Turtle

ICON_LOC = "ship.gif"

MOVEMENT_SIZE = 20


class Ship(Turtle):
    def __init__(self, screen_obj):
        super().__init__()

        self.screen = screen_obj
        self.penup()
        self.screen.addshape(ICON_LOC)
        self.shape(ICON_LOC)

    def move_right(self):
        x_cor = self.xcor() + MOVEMENT_SIZE
        self.setx(x_cor)
