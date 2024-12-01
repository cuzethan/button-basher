import arcade

# Constants
BUTTON_IMAGE = "assets/button.png"
BUTTON_CLICK_SOUND = "assets/click sound.wav"

class ButtonSection(arcade.Section):

    def __init__(self, left: int, bottom: int, width: int, height: int, game_view, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.game_view = game_view #will give us access to all data

        # Variables that will hold sprite lists
        """ Set up the game and initialize the variables. """
        self.button_sprite = arcade.Sprite(BUTTON_IMAGE)
        self.button_sprite.center_x = self.left + (self.width // 2)
        self.button_sprite.center_y = self.height // 2
        self.button_sprite.scale = 1.0  # Default scale

        #self.background_image = arcade.load_texture("assets/button_section.png")  # Load background image

        # Load the button click sound
        self.button_click_sound = arcade.load_sound(BUTTON_CLICK_SOUND)
        
        # Animation-related attributes
        self.scale_target = 1.0  # Target scale for animation
        self.scale_speed = 5.0  # Speed of scaling animation

    def on_draw(self):
         # Draw the background image
        #arcade.draw_lrwh_rectangle_textured(self.left, self.bottom, self.width, self.height, self.background_image)
        self.button_sprite.draw()
        arcade.draw_text(f"{self.name}'s Button Factory", self.left, self.window.height - 60, 
            arcade.color.BLACK, 25, width=self.width, align="center")
        arcade.draw_text(f"{int(self.game_view.score)} Buttons", self.left, self.window.height // 2 + 200, 
            arcade.color.BLACK, 25, width=self.width, align="center")
        arcade.draw_text(f"{self.game_view.score_per_sec} Buttons Per Sec", self.left, self.window.height // 2 + 160, 
            arcade.color.BLACK, 20, width=self.width, align="center")
        
    def on_update(self, delta_time):
        # Increment score automatically based on score_per_sec
        self.game_view.score += self.game_view.score_per_sec * delta_time

        # Smoothly scale the button sprite
        if self.button_sprite.scale != self.scale_target:
            if self.button_sprite.scale < self.scale_target:
                self.button_sprite.scale += self.scale_speed * delta_time
                if self.button_sprite.scale > self.scale_target:
                    self.button_sprite.scale = self.scale_target
            elif self.button_sprite.scale > self.scale_target:
                self.button_sprite.scale -= self.scale_speed * delta_time
                if self.button_sprite.scale < self.scale_target:
                    self.button_sprite.scale = self.scale_target

        # Reset scale_target to the default size after animation
        if self.button_sprite.scale == self.scale_target and self.scale_target != 1.0:
            self.scale_target = 1.0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.button_sprite.collides_with_point((x, y)):
            self.game_view.score += (self.game_view.click_value * self.game_view.click_multi)
            self.scale_target = 0.9  # Shrink the button when clicked

            # Play the click sound
            arcade.play_sound(self.button_click_sound)
