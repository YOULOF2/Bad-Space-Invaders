class Globals:
    def __init__(self):
        self.ship_obj = None
        self.gm_obj = None
        self.alien_dealer_obj = None
        self.screen_obj = None

    def register(self, **kwargs):
        ship = kwargs.get("ship")
        gm = kwargs.get("gm")
        alien_dealer = kwargs.get("alien_dealer")
        screen = kwargs.get("screen")

        print(ship, gm, alien_dealer, screen)

        if self.ship_obj is None:
            self.ship_obj = ship

        if self.gm_obj is None:
            self.gm_obj = gm

        if self.alien_dealer_obj is None:
            self.alien_dealer_obj = alien_dealer

        if self.screen_obj is None:
            self.screen_obj = screen


global_vars = Globals()
