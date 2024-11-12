import arcade

#constants

class UpgradeSection(arcade.Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        # Variables that will hold sprite lists
        """ Set up the game and initialize the variables. """

        # Set up the player info

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.ORANGE)
        arcade.draw_text("Upgrades", self.left, self.window.height - 60, 
            arcade.color.BLACK, 25, width=self.width, align="center")
