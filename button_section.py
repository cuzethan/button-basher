import arcade

#constants
BUTTON_IMAGE = "button.png"

class ButtonSection(arcade.Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        # Variables that will hold sprite lists
        """ Set up the game and initialize the variables. """
        self.button_sprite = arcade.Sprite(BUTTON_IMAGE)
        self.button_sprite.center_x = self.left + (self.width // 2)
        self.button_sprite.center_y = self.height // 2

        # Set up the player info
        self.score = 0

        print("left", left)
        print("bottom", bottom)
        print("width", width)
        print("height", height)

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.GRAY)
        self.button_sprite.draw()
        arcade.draw_text(f"Score: {self.score}", self.width, self.window.height // 2 + 150, 
            arcade.color.BLACK, 20, width=self.width, align="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.button_sprite.collides_with_point((x,y)):
            self.score += 1
            print (f"Button Clicked! Current score: {self.score}")
