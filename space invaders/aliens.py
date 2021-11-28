from turtle import Turtle
from random import randint
from time import sleep
import gc

SLEEP_TIME = 1
ALIEN_MOVE_DISTANCE = 25
TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y = 1000, 1000


class AlienBaseClass(Turtle):
    def __init__(self):
        super(AlienBaseClass, self).__init__()
        self.penup()

        self.screen = self.getscreen()

    def move(self):
        sleep(SLEEP_TIME)
        current_coord = self.ycor()
        self.sety(current_coord - ALIEN_MOVE_DISTANCE)
        self.screen.update()

        if self.ycor() < -400:
            self.hideturtle()
            self.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
            self.screen.update()
            del self
            gc.collect()
            return

    #


class Alien1(AlienBaseClass):
    ICON = "images/alien1.gif"

    def __init__(self):
        super(Alien1, self).__init__()
        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


class Alien2(AlienBaseClass):
    ICON = "images/alien2.gif"

    def __init__(self):
        super(Alien2, self).__init__()

        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


class Alien3(AlienBaseClass):
    ICON = "images/alien3.gif"

    def __init__(self):
        super(Alien3, self).__init__()

        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


ALIEN1_START, ALIEN1_END = 30, 30
ALIEN2_START, ALIEN2_END = 0, 20
ALIEN3_START, ALIEN3_END = 0, 10
START_COORD_X, START_COORD_Y = -350, 360


def gen_level():
    aliens_1 = [Alien1 for _ in range(randint(ALIEN1_START, ALIEN1_END))]
    aliens_2 = [Alien2 for _ in range(randint(ALIEN2_START, ALIEN2_END))]
    aliens_3 = [Alien3 for _ in range(randint(ALIEN3_START, ALIEN3_END))]

    step_x, step_y = 0, 0
    alien_objs = []

    for alien in aliens_1:
        alien_obj = alien()
        alien_obj.goto(START_COORD_X + step_x, START_COORD_Y + step_y)
        alien_obj.showturtle()
        alien_obj.screen.update()

        alien_objs.append(alien_obj)

        if alien_obj.xcor() > 330:
            step_y -= 50
            step_x = 0
            print(step_y)
        else:
            step_x += 50

    [alien_obj.move() for alien_obj in alien_objs]
