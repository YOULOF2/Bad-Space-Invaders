from turtle import Turtle
from datetime import datetime
from time import sleep
import gc

PLAYER_MOVEMENT_SIZE: int = 20
BULLET_MOVE_DISTANCE: int = 20
STARTING_YCOR: int = -340
SLEEP_TIME: float = 0.01

BULLET_FREQUENCY: int = 600000

PLAYER_SHAPE, BULLET_SHAPE = "images/player.gif", "images/player_bullet.gif"


#   TODO: Create Bullets
class Bullet(Turtle):
    def __init__(self, player_coord: tuple):
        super(Bullet, self).__init__()

        self.penup()
        self.goto(player_coord[0], player_coord[1])
        self.speed(0)

        self.screen = self.getscreen()
        self.screen.register_shape(BULLET_SHAPE)
        self.shape(BULLET_SHAPE)

        self.screen.update()

        self._move()

    def _move(self):
        moving = True
        while moving:
            sleep(SLEEP_TIME)
            self.screen.update()
            current_coord = self.ycor()
            self.sety(current_coord + BULLET_MOVE_DISTANCE)

            if self.ycor() > 410:
                self.hideturtle()
                moving = False
                self.screen.update()
        del self
        gc.collect()


# TODO: Create Player Class
class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()

        self.penup()
        self.speed(0)
        self.sety(STARTING_YCOR)

        self.last_bullet_shot = []
        self.last_bullet_shot.append(self._return_last_bullet("left"))
        self.screen = self.getscreen()
        self.screen.register_shape(PLAYER_SHAPE)
        self.shape(PLAYER_SHAPE)

        self.screen.update()

    def _turret(self):
        if self.last_bullet_shot[-1].get("gun") == "right":
            self.last_bullet_shot.append(self._return_last_bullet("right"))
            current_coordinates = (self.xcor() + 12, self.ycor())
            Bullet(current_coordinates)
        elif self.last_bullet_shot[-1].get("gun") == "left":
            self.last_bullet_shot.append(self._return_last_bullet("left"))
            current_coordinates = (self.xcor() - 12, self.ycor())
            Bullet(current_coordinates)

    @staticmethod
    def _return_last_bullet(gun):
        if gun == "right":
            return {
                "gun": "left",
                "last_bullet": datetime.now()
            }
        else:
            return {
                "gun": "right",
                "last_bullet": datetime.now()
            }

    #   TODO: Add Movement
    def move_right(self):
        current_x = self.xcor()
        self.setx(current_x + PLAYER_MOVEMENT_SIZE)

        if self.xcor() > 390:
            self.setx(-400)

        self.screen.update()

    def move_left(self):
        current_x = self.xcor()
        self.setx(current_x - PLAYER_MOVEMENT_SIZE)

        if self.xcor() < -390:
            self.setx(400)

        self.screen.update()

    #   TODO: Create Bullet
    def shoot_bullet(self):
        time_dif = (datetime.now() - self.last_bullet_shot[-1].get("last_bullet")).microseconds
        if time_dif >= BULLET_FREQUENCY:
            self._turret()
