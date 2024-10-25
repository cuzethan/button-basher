import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "BUTTON CLICKER GAME"
BUTTON_IMAGE = "button.png" 

class ButtonClickerGame(arcade.Window):
    def __init__ (self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.button_sprite = None

    def setup(self):
        self.button_sprite = arcade.Sprite(BUTTON_IMAGE, scale = 0.2)
        self.button_sprite.center_x = SCREEN_WIDTH // 2
        self.button_sprite.center_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()
        self.button_sprite.draw()

    def on_update(self, delta_time):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        if self.button_sprite.collides_with_point((x,y)):
            print ("Button Clicked!")

def main():
    game = ButtonClickerGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()