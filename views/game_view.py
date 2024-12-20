import arcade
from views.sections import UpgradeSection, ButtonSection

class GameView(arcade.View):
    def __init__(self, name):
        super().__init__()
        # Factory Name
        self.name = name 

        # TOTAL SCORE
        self.score = 0 

        # Click value, auto value, and its multipliers
        self.score_per_sec = 0
        self.score_per_sec_multi = 1
        self.click_value = 1
        self.click_multi = 1
        
        # Pass `self` as the game_view argument to UpgradeSection & ButtonSection
        self.add_section(ButtonSection(self.window.width / 2, 0, self.window.width / 2, self.window.height, name=self.name, game_view=self))
        self.add_section(UpgradeSection(0, 0, self.window.width / 2, self.window.height, game_view=self))
