import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "BUTTON CLICKER GAME"
BUTTON_IMAGE = "button.png" 

class ButtonClickerGame(arcade.Window):
    def __init__ (self):
        super().__init__(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        pass


    def on_draw(self):
        arcade.start_render();

    def on_update(self, delta_time):
        pass

def main():
    game = ButtonClickerGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()