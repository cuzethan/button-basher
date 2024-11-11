import arcade
from start_view import StartView

# --- Constants ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
SCREEN_TITLE = "BUTTON BASHER"

def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()