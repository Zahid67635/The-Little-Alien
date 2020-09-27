class settings:
    def __init__(self):

        """Initialize the game's static settings."""
        #screen settings

        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.ship_speed = 8.5
        self.ship_limit = 3

        #bullet settings

        self.bullet_speed = 6.5
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color =(255,0,0)
        self.bullets_allowed = 20

        self.alien_speed = 3.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
         """Initialize settings that change throughout the game."""
         self.ship_speed = 8.5
         self.bullet_speed = 6.5
         self.alien_speed = 3.0
         # fleet_direction of 1 represents right; -1 represents left.
         self.fleet_direction = 1
         self.alien_points = 50

    def increase_speed(self):
         """Increase speed settings."""
         self.ship_speed *= self.speedup_scale
         self.bullet_speed *= self.speedup_scale
         self.alien_speed *= self.speedup_scale
         self.alien_points = int(self.alien_points * self.score_scale)
         print(self.alien_points)
