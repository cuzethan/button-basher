import arcade

#constants
BUTTON_IMAGE = "button.png"

class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Set screen dimensions
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        # Variables that will hold sprite lists
        self.button_sprite = None

        # Set up the player info
        self.score = 0

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.button_sprite = arcade.Sprite(BUTTON_IMAGE)
        self.button_sprite.center_x = self.SCREEN_WIDTH // 2
        self.button_sprite.center_y = self.SCREEN_HEIGHT // 2

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.button_sprite.draw()
        arcade.draw_text(f"Score: {self.score}", 10, self.SCREEN_HEIGHT-30, arcade.color.BLACK, 20)

    def on_update(self, delta_time):
        pass
    
    def on_mouse_press(self, x, y, button, modifiers):
        if self.button_sprite.collides_with_point((x,y)):
            self.score += 1
            print (f"Button Clicked! Current score: {self.score}")