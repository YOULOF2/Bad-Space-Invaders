import pathlib
from time import sleep
from turtle import Turtle

from global_vars import global_vars

ENEMY1_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy1.gif"
ENEMY2_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy2.gif"
ENEMY3_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy3.gif"
ENEMY4_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy4.gif"
ENEMY_BULLET = f"{pathlib.Path(__file__).parent.resolve()}/icons/bullet.gif"

DISTANCE_FROM_BORDER = 50

BOUNCE_BORDER_X = 500

START_X = -500

TRAVEL_DISTANCE = 50

DISTANCE_FROM_PLAYER = 100

TIME_BETWEEN_MOVING = 0.1

MOVEMENT_SIZE = 30

SHAPE_SIZE = 3

ALLOWED_TIME_RANGE = 500000

SPEED = 10

MOVE_DISTANCE = 20

SLEEP_TIME = 0.009

SHIP_LIVES = 3

DISTANCE_FROM_ALIENS = 100


class EnemyBullet(Turtle):
    def __init__(self, start_coord: list):
        super().__init__()

        self.screen = global_vars.screen_obj
        self.ship = global_vars.ship_obj

        self.penup()
        self.setheading(270)
        self.goto(start_coord[0], start_coord[1])

        self.screen.register_shape(ENEMY_BULLET)
        self.shape(ENEMY_BULLET)
        self.hideturtle()

    def return_obj(self):
        return self

    def move(self):
        self.showturtle()
        for _ in range(60):
            sleep(SLEEP_TIME)
            self.forward(MOVE_DISTANCE)
            self.screen.update()

            if self.distance(self.ship) < DISTANCE_FROM_PLAYER:
                self.ship.lives -= 1
                print(f"ship health: {self.ship.lives}")

                if self.ship.lives == 0:
                    self.hideturtle()
                    self.ship.hideturtle()

                    self.screen.update()
                    del self.ship
                    return

                self.hideturtle()
                self.screen.update()
                del self
                return


class Enemy1(Turtle):
    __slots__ = "screen", "health", "ship", "bullets_shot"

    def __init__(self):
        super().__init__()

        self.screen = global_vars.screen_obj
        self.health = 1
        self.ship = global_vars.ship_obj
        self.bullets_shot = []

        self.hideturtle()
        self.screen.register_shape(ENEMY1_ICON)
        self.shape(ENEMY1_ICON)
        self.penup()

    def shoot(self):
        coordinates = [self.xcor(), self.ycor()]
        bullet_obj = EnemyBullet(start_coord=coordinates)
        self.bullets_shot.append(bullet_obj.return_obj())

        bullet_obj.move()


class Enemy2(Turtle):
    __slots__ = "screen", "health"

    def __init__(self):
        super().__init__()

        self.screen = global_vars.screen_obj
        self.health = 2

        self.hideturtle()
        self.screen.register_shape(ENEMY2_ICON)
        self.shape(ENEMY2_ICON)
        self.penup()


class Enemy3(Turtle):
    __slots__ = "screen", "health"

    def __init__(self):
        super().__init__()

        self.screen = global_vars.screen_obj
        self.health = 3

        self.hideturtle()
        self.screen.register_shape(ENEMY3_ICON)
        self.shape(ENEMY3_ICON)
        self.penup()


class Enemy4(Turtle):
    __slots__ = "screen", "health"

    def __init__(self):
        super().__init__()

        self.screen = global_vars.screen_obj
        self.health = 5

        self.hideturtle()
        self.screen.register_shape(ENEMY4_ICON)
        self.shape(ENEMY4_ICON)
        self.penup()


class AlienDealer:
    __slots__ = "screen", "__current_level", "alien_list", "stage_list", "__level_sequencer"

    def __init__(self):
        self.screen = global_vars.screen_obj

        self.alien_list = []
        self.__current_level = "level 1"

        self.stage_list = [self.__level1, self.__level2, self.__level3, self.__level4]
        self.__level_sequencer = self.__stage_gen()

    @property
    def current_level(self):
        return self.__current_level

    # ==================== Stage generators ====================
    def __stage_gen(self):
        for stage in self.stage_list:
            yield stage

    def next_stage(self):
        next_stage = next(self.__level_sequencer)
        next_stage()

    # ==================== levels  ====================
    def __level1(self):
        first_start_x = START_X
        second_start_x = START_X
        for num in range(22):
            if num <= 10:
                alien = Enemy1()
                alien.goto(first_start_x, 300)
                first_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)
            else:
                alien = Enemy1()
                alien.goto(second_start_x, 200)
                second_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)

        self.screen.update()

    def __level2(self):
        first_start_x = START_X
        second_start_x = START_X
        third_start_x = START_X

        for num in range(11):
            alien = Enemy2()
            alien.goto(first_start_x, 300)
            first_start_x += DISTANCE_FROM_ALIENS
            alien.showturtle()
            self.alien_list.append(alien)

        for num in range(22):
            if num <= 10:
                alien = Enemy1()
                alien.goto(third_start_x, 200)
                third_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)
            else:
                alien = Enemy1()
                alien.goto(second_start_x, 100)
                second_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)

        self.screen.update()

    def __level3(self):
        return NotImplemented

    def __level4(self):
        return NotImplemented
