import arcade
from logic.single_upgrade import *
from logic.stackable_upgrade import *

class UpgradeSection(arcade.Section):
    def __init__(self, left: int, bottom: int, width: int, height: int, game_view, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.game_view = game_view

        #All upgrades
        self.auto_clicker = AutoClicker()
        self.double_clicker = DoubleClicker()
        self.mega_auto_clicker = MegaAutoClicker()
        self.factory_workers = FactoryWorker()
        
    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.ORANGE)
        arcade.draw_text("Upgrades", self.left, self.window.height - 60, 
                        arcade.color.BLACK, 25, width=self.width, align="center")

        # AutoClicker Upgrade
        arcade.draw_text(self.auto_clicker.getDesc(), self.left + 20, self.top - 100, 
                        self.auto_clicker.getColor(), 16)

        # DoubleClicker Upgrade
        arcade.draw_text(self.double_clicker.getDesc(), self.left + 20, self.top - 140, 
                        self.double_clicker.getColor(), 16)
        
        # Draw Mega Autoclicker Upgrade
        arcade.draw_text(self.mega_auto_clicker.getDesc(), self.left + 20, self.top - 180, 
                        self.mega_auto_clicker.getColor(), 16)

        # Draw Factory Worker Upgrade
        arcade.draw_text(self.factory_workers.getDesc(), self.left + 20, self.top - 220, 
                        self.factory_workers.getColor(), 16)

    def on_mouse_press(self, x, y, button, modifiers):
        # Check for AutoClicker purchase
        if (self.left + 20 < x < self.left + 180 and self.top - 110 < y < self.top - 90):
            self.auto_clicker.activate(self.game_view) # activate upgrade

        # Check for DoubleClicker purchase
        if (self.left + 20 < x < self.left + 180 and self.top - 150 < y < self.top - 130):
            self.double_clicker.activate(self.game_view) # activate upgrade

        # Check for MegaAutoClicker purchase
        if (self.left + 20 < x < self.left + 180 and self.top - 190 < y < self.top - 170):
            self.mega_auto_clicker.activate(self.game_view) # activate upgrade

        # Check for Factory Worker purchase
        if (self.left + 20 < x < self.left + 180 and self.top - 230 < y < self.top - 210):
            self.factory_workers.activate(self.game_view)

