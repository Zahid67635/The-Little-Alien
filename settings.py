class settings:
    def __init__(self):
        #screen settings

        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bullet settings

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color =(0,0,0)
        self.bullets_allowed = 20

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
