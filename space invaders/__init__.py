from turtle import Screen
from game_manager import GameManager
from player import Ship
import logging
from aliens import AlienDealer

logging.basicConfig(filename="logfile.log", encoding="utf-8", level=logging.DEBUG, format="%(levelname)s: %(message)s")

BACKGROUND_IMG = "icons/background.gif"

screen = Screen()
screen.setup(width=1200, height=780)
screen.bgpic(BACKGROUND_IMG)
screen.tracer(0)

screen_width = screen.window_width()
screen_height = screen.window_height()

alien_dealer = AlienDealer(screen)
ship = Ship(screen, alien_dealer)
gm = GameManager(screen, screen_width, screen_height, ship, alien_dealer)

screen.listen()
screen.onkey(ship.move_right, "d")
screen.onkey(ship.move_left, "a")
screen.onkey(ship.shoot, "space")

if __name__ == "__main__":
    screen.mainloop()
