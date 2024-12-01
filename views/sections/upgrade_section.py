import arcade
from logic.single_upgrade import *
from logic.stackable_upgrade import *

class UpgradeSection(arcade.Section):
    def __init__(self, left: int, bottom: int, width: int, height: int, game_view, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.game_view = game_view

        #Upgrades list, each tuple contains upgrade and y_offset
        self.upgrades = [
            (AutoClicker(), 100),
            (DoubleClicker(), 150),
            (MegaAutoClicker(), 200),
            (FactoryWorker(), 250)
        ]
        
    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.ORANGE)
        arcade.draw_text("Upgrades", self.left, self.window.height - 60, 
                        arcade.color.BLACK, 25, width=self.width, align="center")

        # Iterate through upgrades and draw them dynamically
        for upgrade, y_offset in self.upgrades:
            arcade.draw_text(upgrade.getDesc(), self.left + 20, self.top - y_offset, 
                        upgrade.getColor(), 16)
            arcade.draw_lrtb_rectangle_outline(self.left + 10, self.right - 10, self.top - (y_offset - 25),
                        self.top - (y_offset + 7.5), arcade.color.BLACK, 2)

    def on_mouse_press(self, x, y, button, modifiers):
        # Iterate through upgrades and check if they were clicked
        for upgrade, y_offset in self.upgrades:
            if (self.left + 10 < x < self.right - 10 and self.top - (y_offset + 7.5) < y < self.top - (y_offset - 25)):
                upgrade.activate(self.game_view)
