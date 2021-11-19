from turtle import Screen
from game_manager import GameManager
from player.player import Ship

BACKGROUND_IMG = "icons/background.gif"

screen = Screen()
screen.setup(width=1200, height=780)
screen.bgpic(BACKGROUND_IMG)

screen_width = screen.window_width()
screen_height = screen.window_height()

GameManager(screen, screen_width, screen_height)

ship = Ship(screen)

screen.mainloop()
