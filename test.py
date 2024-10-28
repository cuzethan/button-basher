import random
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "BUTTON BASHER"
BUTTON_IMAGE = "button.png"


class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists
        self.button_sprite = None

        # Set up the player info
        self.score = 0

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.button_sprite = arcade.Sprite(BUTTON_IMAGE)
        self.button_sprite.center_x = SCREEN_WIDTH // 2
        self.button_sprite.center_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.button_sprite.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT-30, arcade.color.BLACK, 20)

    def on_update(self, delta_time):
        pass
    
    def on_mouse_press(self, x, y, button, modifiers):
        if self.button_sprite.collides_with_point((x,y)):
            self.score += 1
            print (f"Button Clicked! Current score: {self.score}")

class StartView(arcade.View):
    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height) 

         # Button dimensions
        self.button_x = self.window.width / 2
        self.button_y = self.window.height / 2 - 100
        self.button_width = 200
        self.button_height = 50  

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        # Draw the button
        arcade.draw_rectangle_filled(self.button_x, self.button_y, 
                                     self.button_width, self.button_height, 
                                     arcade.color.LIGHT_GRAY)
        arcade.draw_text("Start Game", self.button_x, self.button_y, 
                         arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, x, y, button, modifiers):
        """ Check if the button is clicked """
        if (self.button_x - self.button_width / 2 < x < self.button_x + self.button_width / 2 and
            self.button_y - self.button_height / 2 < y < self.button_y + self.button_height / 2):
            # Start the game if the button is clicked
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()