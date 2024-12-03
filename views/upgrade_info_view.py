import arcade
from logic.single_upgrade import *
from logic.stackable_upgrade import *

class UpgradeInfoView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view # Set paramater as game_view
        
        # Single upgrades list, each tuple contains upgrade and y_offset
        self.single_upgrades = [
            (AutoClicker(), 100),
            (MegaAutoClicker(), 140),
            (ButtonGear(), 180),
            (ButtonBooster(), 220),
            (ButtonEvolver(), 260),
        ]

        # Stackable upgrades list, same concept as above 
        self.stackable_upgrades = [
            (FactoryWorker(), 360),
            (ButtonMachine(), 400),
            (PowerGenerator(), 440),
            (ButtonBoss(), 480),
            (ButtonFactory(), 520),
            (ButtonBashMilk(), 560)
        ]

    def on_draw(self):
        """ Draw the popup input screen """
        arcade.start_render()

        # Loops through all the upgrades and writes information on what each upgrade does
        arcade.draw_text("Single Upgrades", 40, self.window.height - 60, arcade.color.BLACK, 40, font_name="Jersey 15")
        for upgrade, y_offset in self.single_upgrades:
            arcade.draw_text(upgrade.getFullHelpText(), 60, self.window.height - y_offset, upgrade.getColor(), 20, font_name="Jersey 15")

        arcade.draw_text("Stackable Upgrades", 40, self.window.height - 320, arcade.color.BLACK, 40, font_name="Jersey 15")
        for upgrade, y_offset in self.stackable_upgrades:
            arcade.draw_text(upgrade.getFullHelpText(), 60, self.window.height - y_offset, upgrade.getColor(), 20, font_name="Jersey 15")

        # Button to go back to game view
        arcade.draw_rectangle_filled(self.window.width - 90, 40, 125, 35, arcade.color.LIGHT_PINK)
        arcade.draw_rectangle_outline(self.window.width - 90, 40, 125, 35, arcade.color.BLACK, 4)
        arcade.draw_text("Go Back", self.window.width - 147.5, 30, arcade.color.BLACK, 30, font_name="Jersey 15")

    def on_mouse_press(self, x, y, button, modifiers):
        # If button is pressed, go back to game view
        if self.window.width - 155 <= x <= self.window.width - 35 and 20 <= y <= 60:
            self.window.show_view(self.game_view)