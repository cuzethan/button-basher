import arcade
import arcade.color
from views import GameView
import importlib

class NameInputView(arcade.View):
    def __init__(self, shared_sound, sound_player):
        super().__init__()
        self.user_input = ""  # Store the user's name input
        self.background_image = arcade.load_texture("assets/background_image.png") # Blured background
        self.start_sound = shared_sound # Start sound 
        self.sound_player = sound_player # The sound player (bring it to this view keeps music going)

    def on_draw(self):
        """ Draw the popup input screen """
        arcade.start_render()

        # Draw the background image
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background_image)

        arcade.draw_text("Enter your name:", self.window.width / 2, self.window.height / 2 + 10,
                         arcade.color.BLACK, 40, font_name="Jersey 15", anchor_x="center", bold = True)
        
        # Draw the current input text
        arcade.draw_text(self.user_input, self.window.width / 2, self.window.height / 2 - 30,
                         arcade.color.YELLOW_ROSE, 30, font_name="Jersey 15", anchor_x="center", bold = True)
        
        # Instruction text
        arcade.draw_text("Press Enter to confirm", self.window.width / 2, self.window.height / 2 - 70,
                         arcade.color.BLACK, 25, font_name="Jersey 15", anchor_x="center", bold= True)      

    def on_key_press(self, key, modifiers):
        """ Handle user input """
        if key == arcade.key.ENTER:
            # Stop sound after user enters name
            if self.sound_player:
                self.start_sound.stop(self.sound_player)
    
            # When Enter is pressed, move to game view with the final input as parameter
            self.window.show_view(GameView(self.user_input))
        elif key == arcade.key.BACKSPACE:
            # Remove the last character from the input
            self.user_input = self.user_input[:-1]
        else:
            # Handle printable characters (letters, numbers, space)
            if len(self.user_input) < 15:  # Optional: limit name length
                if 32 <= key <= 126:  # Check if key is a printable ASCII character
                    # Check if Shift is pressed for capital letters
                    if modifiers & arcade.key.MOD_SHIFT:  # Shift is pressed
                        if 97 <= key <= 122:  # Lowercase letter
                            key -= 32  # Convert to uppercase by changing ASCII value
                    self.user_input += chr(key)
