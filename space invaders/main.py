from turtle import Screen
from window_manager import WinManager

BACKGROUND_IMG = "icons/background.gif"

screen = Screen()
screen.setup(width=1200, height=780)
screen.bgpic(BACKGROUND_IMG)

screen_width = screen.window_width()
screen_height = screen.window_height()

win_manager = WinManager(screen, screen_width, screen_height)

print("HELLO")

screen.mainloop()
