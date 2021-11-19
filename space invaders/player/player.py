from turtle import Turtle
from .bullet import Bullet
from datetime import datetime

MOVEMENT_SIZE = 20

DISTANCE_FROM_BORDER = 50

SHAPE_SIZE = 3

ALLOWED_TIME_RANGE = 600000


class Ship(Turtle):
    def __init__(self, screen_obj):
        super().__init__()

        self.screen = screen_obj
        self.penup()
        self.hideturtle()
        self.speed(0)

        self.screen_width = self.screen.window_width()

        self.last_bullet = []
        self.is_init = False

    def init(self, half_height):
        self.shape("circle")
        self.shapesize(SHAPE_SIZE)
        self.color("white")
        self.sety(DISTANCE_FROM_BORDER - half_height)
        self.showturtle()
        self.screen.update()

        self.is_init = True

    def move_right(self):
        if self.is_init:
            x_cor = self.xcor() + MOVEMENT_SIZE
            self.setx(x_cor)

            if self.xcor() > (self.screen_width / 2):
                self.hideturtle()
                self.setx(-self.screen_width / 2)
                self.showturtle()
            self.screen.update()

    def move_left(self):
        if self.is_init:
            x_cor = self.xcor() - MOVEMENT_SIZE
            self.setx(x_cor)

            if (self.xcor() < -600) and (self.xcor() < (self.screen_width / 2)):
                self.hideturtle()
                self.setx(self.screen_width / 2)
                self.showturtle()
            self.screen.update()

    def shoot(self):
        if self.is_init:
            coordinates = [self.xcor(), self.ycor()]
            bullet = Bullet(coordinates, self.screen)

            try:
                time_dif = (datetime.now() - self.last_bullet[-1]).microseconds
                print(time_dif)
            except IndexError:
                self.last_bullet.append(datetime.now())
                bullet.move()
            else:
                if time_dif > ALLOWED_TIME_RANGE:
                    self.last_bullet.append(datetime.now())
                    bullet.move()
