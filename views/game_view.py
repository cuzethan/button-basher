import arcade
from views.sections import UpgradeSection, ButtonSection
from .upgrades import AutoClicker, DoubleClicker

class GameView(arcade.View):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0
        self.click_value = 1
        self.auto_clicker = AutoClicker()
        self.double_clicker = DoubleClicker()

        # Store ButtonSection as an attribute to access it in UpgradeSection
        self.button_section = ButtonSection(self.window.width / 2, 0, self.window.width / 2, self.window.height, name=self.name)
        self.add_section(self.button_section)
        
        # Pass `self` as the game_view argument to UpgradeSection
        self.add_section(UpgradeSection(0, 0, self.window.width / 2, self.window.height, game_view=self))



    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time):
        self.auto_clicker.apply(self)
    def on_mouse_press(self, x, y, button, modifiers):
        # Update score by click value (1 or 2 based on DoubleClicker upgrade)
        self.score += self.click_value