import arcade
from views import StartView

# --- Constants ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
SCREEN_TITLE = "BUTTON BASHER"

def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) # Set dimensions and name of window
    window.center_window() # Center it
    start_view = StartView() # Set start view
    window.show_view(start_view) # Show start view
    arcade.run() # Run arcade


if __name__ == "__main__":
    main()