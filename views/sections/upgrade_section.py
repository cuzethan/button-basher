import arcade
from logic.single_upgrade import *
from logic.stackable_upgrade import *
from views.upgrade_info_view import UpgradeInfoView

class UpgradeSection(arcade.Section):
    def __init__(self, left: int, bottom: int, width: int, height: int, game_view, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.game_view = game_view
        self.buy_amount = 1 # Default buy amount (quantity-wise)
        self.highlight_y_value = None
        self.background_image = arcade.load_texture("assets/upgrade_background.jpg")  # Load background image

         # Load the upgrade purchase sound
        self.purchase_sound = arcade.load_sound("assets/upgrade_sound.wav")

        #Upgrades list, each tuple contains upgrade and y_offset
        self.upgrades = [
            (AutoClicker(), 130),
            (MegaAutoClicker(), 180),
            (ButtonGear(), 230),
            (ButtonBooster(), 280),
            (ButtonEvolver(), 330),
            (FactoryWorker(), 380),
            (ButtonMachine(), 430),
            (PowerGenerator(), 480),
            (ButtonBoss(), 530),
            (ButtonFactory(), 580),
            (ButtonBashMilk(), 630)
        ]
                
    def on_draw(self):
        # Draw the background image
        arcade.draw_lrwh_rectangle_textured(self.left, self.bottom, self.width, self.height, self.background_image)

        # Set "Upgrades" title
        arcade.draw_text("Upgrades", self.left, self.window.height - 60, 
                        arcade.color.BLACK, 32.5, font_name="Jersey 15", width=self.width, align="center")

        # Draw buttons for buy multiplier buttons 
        arcade.draw_text("Buy 1", 72.5, self.window.height - 90, arcade.color.GREEN if self.buy_amount == 1 else arcade.color.BLACK, 20, font_name="Jersey 15")
        arcade.draw_text("Buy 10", 272.5, self.window.height - 90, arcade.color.GREEN if self.buy_amount == 10 else arcade.color.BLACK, 20, font_name="Jersey 15")
        arcade.draw_text("Buy 100", 472.5, self.window.height - 90, arcade.color.GREEN if self.buy_amount == 100 else arcade.color.BLACK, 20, font_name="Jersey 15")

        # Draw button for upgrade stats
        arcade.draw_text("What do upgrades do?", 180, 60, arcade.color.BLACK, 20, bold=True, font_name="Jersey 15")
        arcade.draw_lrtb_rectangle_outline(self.width/2 - 125, self.width/2 + 125, 80, 55, arcade.color.BLACK, 2)

        # Iterate through upgrades and draw them dynamically
        for upgrade, y_offset in self.upgrades:
            if isinstance(upgrade, StackableUpgrade): # Will draw text specifically for stackable upgrades
                arcade.draw_text(upgrade.getDesc(self.buy_amount), self.left + 20, self.top - y_offset, upgrade.getColor(), 20, font_name="Jersey 15")
            else: # Draw text for single upgrades
                arcade.draw_text(upgrade.getDesc(), self.left + 20, self.top - y_offset, upgrade.getColor(), 20, font_name="Jersey 15")
            arcade.draw_lrtb_rectangle_outline(self.left + 10, self.right - 10, self.top - (y_offset - 25), # outline of upgrade boxes
                        self.top - (y_offset + 7.5), arcade.color.BLACK, 2)

            if self.highlight_y_value: # Set highlight for mouse hover on upgrades
                arcade.draw_lrtb_rectangle_filled(self.left + 10, self.right - 10, self.top - (self.highlight_y_value - 25),
                        self.top - (self.highlight_y_value + 7.5), (0, 153, 255, 40))

    def on_mouse_press(self, x, y, button, modifiers):
        # Iterate through upgrades and check if they were clicked
        for upgrade, y_offset in self.upgrades:
            if (self.left + 10 < x < self.right - 10 and self.top - (y_offset + 7.5) < y < self.top - (y_offset - 25)):
                if isinstance(upgrade, StackableUpgrade): #Checks if upgrade is stackable
                    upgrade.activate(self.game_view, self.purchase_sound, self.buy_amount) # Activate upgrade
                else: # Use activate method for single_upgrade
                    upgrade.activate(self.game_view, self.purchase_sound) # Activate upgrade

        # Check if Buy 1 is clicked
        if 72.5 - 10 <= x <= 72.5 + 60 and self.window.height - 90 <= y <= self.window.height - 75:
            self.buy_amount = 1

        # Check if Buy 10 is clicked
        elif 272.5 <= x <= 272.5 + 60 and self.window.height - 90 <= y <= self.window.height - 75:
            self.buy_amount = 10

        # Check if Buy 100 is clicked
        elif 472.5 <= x <= 472.5 + 60 and self.window.height - 90 <= y <= self.window.height - 75:
            self.buy_amount = 100

        # Check if upgrade info button is clicked
        elif 170 <= x <= 420 and 55 <= y <= 80:
            self.window.show_view(UpgradeInfoView(self.game_view))
    
    def on_mouse_motion(self, x, y, dx, dy):
        #sets highlight to none, and checks if mouse is hovering on an upgrade, if it is then set highlight's y_offset to the upgrades's y_offset'
        self.highlight_y_value = None
        for upgrade, y_offset in self.upgrades:
            if (self.left + 10 < x < self.right - 10 and self.top - (y_offset + 7.5) < y < self.top - (y_offset - 25)) and upgrade.active is False:
                self.highlight_y_value = y_offset