import logging
import pathlib
from datetime import datetime
from time import sleep
from turtle import Turtle

from global_vars import global_vars

NORMAL = f"{pathlib.Path(__file__).parent.resolve()}/icons/normal.gif"

MOVEMENT_SIZE = 30

DISTANCE_FROM_BORDER = 50

SHAPE_SIZE = 3

ALLOWED_TIME_RANGE = 500000

SPEED = 10

MOVE_DISTANCE = 20

SLEEP_TIME = 0.009

DISTANCE_FROM_ALIENS = 50

SHIP_LIVES = 3


class Bullet(Turtle):
    __slots__ = "start_coord", "screen", "dealer", "logger"

    def __init__(self, start_coord: list):
        super().__init__()

        self.setheading(90)
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.color("white")
        self.penup()

        self.start_coord = start_coord
        self.goto(self.start_coord[0], self.start_coord[1])

        self.screen = global_vars.screen_obj
        self.dealer = global_vars.alien_dealer_obj

        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.StreamHandler())

    def __is_killed(self):
        if len(self.dealer.alien_list) == 0:
            self.logger.info("All aliens defeated")
            self.dealer.next_stage()

    def move(self):
        self.showturtle()
        for _ in range(60):
            sleep(SLEEP_TIME)
            self.forward(MOVE_DISTANCE)
            self.screen.update()

            for alien in self.dealer.alien_list:
                if self.distance(alien) < DISTANCE_FROM_ALIENS:
                    alien.health -= 1
                    print(f"Alien health: {alien.health}")
                    if alien.health == 0:
                        self.hideturtle()
                        alien.hideturtle()
                        self.dealer.alien_list.remove(alien)

                        self.__is_killed()

                        self.screen.update()
                        del alien
                        return

                    self.hideturtle()
                    self.screen.update()
                    del self
                    return

    def return_obj(self):
        return self


class Ship(Turtle):
    __slots__ = "screen", "screen_width", "last_bullet", "bullets_shot", "alien_dealer", "lives"

    def __init__(self):
        super().__init__()

        self.screen = global_vars.screen_obj
        self.penup()
        self.hideturtle()
        self.speed(0)

        self.screen.register_shape(NORMAL)

        self.__reset_icon()

        self.screen_width = self.screen.window_width()

        self.last_bullet = []
        self.is_init = False
        self.bullets_shot = []
        self.lives = SHIP_LIVES

        self.alien_dealer = global_vars.alien_dealer_obj

    def __reset_icon(self):
        self.shape(NORMAL)

    def init(self, half_height):
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
            self.__reset_icon()
            coordinates = [self.xcor(), self.ycor()]
            bullet_obj = Bullet(coordinates)
            self.bullets_shot.append(bullet_obj.return_obj())

            try:
                time_dif = (datetime.now() - self.last_bullet[-1]).microseconds
            except IndexError:
                self.last_bullet.append(datetime.now())
                bullet_obj.move()
            else:
                if time_dif > ALLOWED_TIME_RANGE:
                    self.last_bullet.append(datetime.now())
                    bullet_obj.move()
