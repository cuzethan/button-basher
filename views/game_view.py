import arcade
from views.sections import UpgradeSection, ButtonSection

class GameView(arcade.View):
    def __init__(self, name):
        super().__init__()
        self.name = name #factory name
        self.score = 0 
        self.score_per_sec = 0
        self.click_value = 1
        self.click_multi = 1

        # Load a background image for the GameView
        self.background_texture = arcade.load_texture("assets/game_background.png")

        # Pass `self` as the game_view argument to UpgradeSection & ButtonSection
        self.add_section(ButtonSection(self.window.width / 2, 0, self.window.width / 2, self.window.height, name=self.name, game_view=self))
        self.add_section(UpgradeSection(0, 0, self.window.width / 2, self.window.height, game_view=self))

    def on_draw(self):
        """Draw the background and all sections"""
        # Draw the background for the entire game view
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background_texture)

        # Call the on_draw methods of each section (automatically handled by `arcade.View`)
        super().on_draw()