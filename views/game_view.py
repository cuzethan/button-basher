import arcade
from views.sections import UpgradeSection, ButtonSection
from .upgrades import AutoClicker, DoubleClicker

class GameView(arcade.View):
    def __init__(self, name):
        super().__init__()
        self.name = name #factory name
        self.score = 0 
        self.score_per_sec = 0
        self.click_value = 1
        self.auto_clicker = AutoClicker()
        self.double_clicker = DoubleClicker()

        # Store ButtonSection as an attribute to access it in UpgradeSection
        self.button_section = ButtonSection(self.window.width / 2, 0, self.window.width / 2, self.window.height, name=self.name, game_view=self)
        self.add_section(self.button_section)
        
        # Pass `self` as the game_view argument to UpgradeSection
        self.add_section(UpgradeSection(0, 0, self.window.width / 2, self.window.height, game_view=self))
