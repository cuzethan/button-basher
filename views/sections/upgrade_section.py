import arcade
from logic.single_upgrade import *
from logic.stackable_upgrade import *

class UpgradeSection(arcade.Section):
    def __init__(self, left: int, bottom: int, width: int, height: int, game_view, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.game_view = game_view
        self.buy_amount = 1
        self.highlight_y_value = None

        #Upgrades list, each tuple contains upgrade and y_offset
        self.upgrades = [
            (AutoClicker(), 130),
            (DoubleClicker(), 180),
            (MegaAutoClicker(), 230),
            (FactoryWorker(), 280)
        ]
        
    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.ORANGE)
        arcade.draw_text("Upgrades", self.left, self.window.height - 60, 
                        arcade.color.BLACK, 25, width=self.width, align="center")

        arcade.draw_text("Buy 1", 67.5, self.window.height - 90, arcade.color.GREEN if self.buy_amount == 1 else arcade.color.BLACK, 15)
        arcade.draw_text("Buy 10", 267.5, self.window.height - 90, arcade.color.GREEN if self.buy_amount == 10 else arcade.color.BLACK, 15)
        arcade.draw_text("Buy 100", 467.5, self.window.height - 90, arcade.color.GREEN if self.buy_amount == 100 else arcade.color.BLACK, 15)

        # Iterate through upgrades and draw them dynamically
        for upgrade, y_offset in self.upgrades:
            arcade.draw_text(upgrade.getDesc(self.buy_amount), self.left + 20, self.top - y_offset, 
                        upgrade.getColor(), 16)
            arcade.draw_lrtb_rectangle_outline(self.left + 10, self.right - 10, self.top - (y_offset - 25),
                        self.top - (y_offset + 7.5), arcade.color.BLACK, 2)

            if self.highlight_y_value:
                arcade.draw_lrtb_rectangle_filled(self.left + 10, self.right - 10, self.top - (self.highlight_y_value - 25),
                        self.top - (self.highlight_y_value + 7.5), (255, 0, 0, 60))

    def on_mouse_press(self, x, y, button, modifiers):
        # Iterate through upgrades and check if they were clicked
        for upgrade, y_offset in self.upgrades:
            if (self.left + 10 < x < self.right - 10 and self.top - (y_offset + 7.5) < y < self.top - (y_offset - 25)):
                if isinstance(obj, StackableUpgrade): #checks if upgrade is stackable
                    upgrade.activate(self.game_view, self.buy_amount)
                else:
                    upgrade.activate(self.game_view)
        
        # Check if Buy 1 is clicked
        if 67.5 <= x <= 67.5 + 60 and self.window.height - 90 <= y <= self.window.height - 75:
            self.buy_amount = 1

        # Check if Buy 10 is clicked
        elif 267.5 <= x <= 267.5 + 70 and self.window.height - 90 <= y <= self.window.height - 75:
            self.buy_amount = 10

        # Check if Buy 100 is clicked
        elif 467.5 <= x <= 467.5 + 85 and self.window.height - 90 <= y <= self.window.height - 75:
            self.buy_amount = 100
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.highlight_y_value = None
        for upgrade, y_offset in self.upgrades:
            if (self.left + 10 < x < self.right - 10 and self.top - (y_offset + 7.5) < y < self.top - (y_offset - 25)) and upgrade.active is False:
                self.highlight_y_value = y_offset