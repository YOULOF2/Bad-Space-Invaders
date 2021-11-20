from turtle import Turtle
import pathlib
from random import randint

ENEMY1_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy1.gif"
ENEMY2_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy2.gif"
ENEMY3_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy3.gif"
ENEMY4_ICON = f"{pathlib.Path(__file__).parent.resolve()}/icons/enemy4.gif"

DISTANCE_FROM_BORDER = 50

BOUNCE_BORDER_X = 500

START_X = -500

TRAVEL_DISTANCE = 50

DISTANCE_FROM_ALIENS = 100


class Enemy1(Turtle):
    def __init__(self, screen_obj):
        super().__init__()

        self.screen = screen_obj

        self.hideturtle()
        self.screen.register_shape(ENEMY1_ICON)
        self.shape(ENEMY1_ICON)
        self.penup()


class Enemy2(Turtle):
    def __init__(self, screen_obj):
        super().__init__()

        self.screen = screen_obj

        self.hideturtle()
        self.screen.register_shape(ENEMY2_ICON)
        self.shape(ENEMY2_ICON)
        self.penup()


class Enemy3(Turtle):
    def __init__(self, screen_obj):
        super().__init__()

        self.screen = screen_obj

        self.hideturtle()
        self.screen.register_shape(ENEMY3_ICON)
        self.shape(ENEMY3_ICON)
        self.penup()


class Enemy4(Turtle):
    def __init__(self, screen_obj):
        super().__init__()

        self.screen = screen_obj

        self.hideturtle()
        self.screen.register_shape(ENEMY4_ICON)
        self.shape(ENEMY4_ICON)
        self.penup()


class AlienDealer:
    def __init__(self, screen_obj):
        self.screen = screen_obj

        self.alien_list = []
        self.__current_level = "level 1"

        self.stage_list = [self.__level1, self.__level2, self.__level3, self.__level4]
        self.__level_sequencer = self.__stage_gen()

    @property
    def current_level(self):
        return self.__current_level

    def __move(self):
        for alien in self.alien_list:
            current_x = alien.xcor()
            alien.setx(current_x + TRAVEL_DISTANCE)
            if current_x >= BOUNCE_BORDER_X or current_x <= (BOUNCE_BORDER_X * -1):
                alien.setx(current_x - TRAVEL_DISTANCE)

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
                alien = Enemy1(self.screen)
                alien.goto(first_start_x, 300)
                first_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)
            else:
                alien = Enemy1(self.screen)
                alien.goto(second_start_x, 200)
                second_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)

    def __level2(self):
        first_start_x = START_X
        second_start_x = START_X
        third_start_x = START_X

        for num in range(11):
            alien = Enemy2(self.screen)
            alien.goto(first_start_x, 300)
            first_start_x += DISTANCE_FROM_ALIENS
            alien.showturtle()
            self.alien_list.append(alien)

        for num in range(22):
            if num <= 10:
                alien = Enemy1(self.screen)
                alien.goto(third_start_x, 200)
                third_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)
            else:
                alien = Enemy1(self.screen)
                alien.goto(second_start_x, 100)
                second_start_x += DISTANCE_FROM_ALIENS
                alien.showturtle()
                self.alien_list.append(alien)

    def __level3(self):
        pass

    def __level4(self):
        pass
