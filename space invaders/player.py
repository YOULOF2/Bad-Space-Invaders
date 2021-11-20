from turtle import Turtle
from datetime import datetime
import pathlib
from time import sleep
import logging

NORMAL = f"{pathlib.Path(__file__).parent.resolve()}/icons/normal.gif"

MOVEMENT_SIZE = 30

DISTANCE_FROM_BORDER = 50

SHAPE_SIZE = 3

ALLOWED_TIME_RANGE = 500000

SPEED = 10

MOVE_DISTANCE = 20

SLEEP_TIME = 0.009

DISTANCE_FROM_ALIENS = 50


class Bullet(Turtle):
    def __init__(self, start_coord: list, screen_obj, alien_dealer):
        super().__init__()

        self.setheading(90)
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.color("white")
        self.penup()

        self.start_coord = start_coord
        self.goto(self.start_coord[0], self.start_coord[1])

        self.screen = screen_obj
        self.dealer = alien_dealer

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
                    self.hideturtle()
                    alien.hideturtle()
                    self.dealer.alien_list.remove(alien)

                    self.__is_killed()

                    self.screen.update()
                    del self
                    del alien

                    return

    def return_obj(self):
        return self


class Ship(Turtle):
    def __init__(self, screen_obj, alien_dealer):
        super().__init__()

        self.screen = screen_obj
        self.penup()
        self.hideturtle()
        self.speed(0)

        self.screen.register_shape(NORMAL)

        self.__reset_icon()

        self.screen_width = self.screen.window_width()

        self.last_bullet = []
        self.is_init = False
        self.bullets_shot = []

        self.alien_dealer = alien_dealer

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
            bullet_obj = Bullet(coordinates, self.screen, self.alien_dealer)
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
