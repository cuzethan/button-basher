import arcade
from game_view import GameView

class NameInputView(arcade.View):
    def __init__(self):
        super().__init__()
        self.user_input = ""  # Store the user's name input

    def on_draw(self):
        """ Draw the popup input screen """
        arcade.start_render()
        arcade.draw_text("Enter your name:", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.BLACK, 20, anchor_x="center")
        
        # Draw the current input text
        arcade.draw_text(self.user_input, self.window.width / 2, self.window.height / 2,
                         arcade.color.BLUE, 20, anchor_x="center")
        
        # Instruction text
        arcade.draw_text("Press Enter to confirm", self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.DARK_GRAY, 14, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """ Handle user input """
        if key == arcade.key.ENTER:
            # When Enter is pressed, handle the input (e.g., save it, print it, or pass it to another view)
            print(f"User entered name: {self.user_input}")
            self.window.show_view(GameView(self.user_input))  # Transition back to main view
        elif key == arcade.key.BACKSPACE:
            # Remove the last character from the input
            self.user_input = self.user_input[:-1]
        else:
            # Add the character to the input if it's a letter, number, or space
            if len(self.user_input) < 15:  # Optional: limit name length
                if 32 <= key <= 126:  # Check if key is a printable ASCII character
                    self.user_input += chr(key)
