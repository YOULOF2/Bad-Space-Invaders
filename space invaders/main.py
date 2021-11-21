import logging
from turtle import Screen

from aliens import AlienDealer
from game_manager import GameManager
from global_vars import global_vars
from player import Ship

logging.basicConfig(filename="logfile.log", encoding="utf-8", level=logging.DEBUG, format="%(levelname)s: %(message)s")

BACKGROUND_IMG = "icons/background.gif"

screen = Screen()
screen.setup(width=1200, height=780)
screen.bgpic(BACKGROUND_IMG)
screen.tracer(0)

screen_width = screen.window_width()
screen_height = screen.window_height()

global_vars.register(screen=screen)
alien_dealer = AlienDealer()
global_vars.register(alien_dealer=alien_dealer)
ship = Ship()
global_vars.register(ship=ship)
gm = GameManager(screen_width, screen_height)
global_vars.register(gm=gm)

screen.listen()
screen.onkey(ship.move_right, "d")
screen.onkey(ship.move_left, "a")
screen.onkey(ship.shoot, "space")

if __name__ == "__main__":
    screen.mainloop()
