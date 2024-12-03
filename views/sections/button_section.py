import arcade

# Constants
BUTTON_IMAGE = "assets/button.png"
BUTTON_CLICK_SOUND = "assets/click_sound.wav"

class ButtonSection(arcade.Section):

    def __init__(self, left: int, bottom: int, width: int, height: int, game_view, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.game_view = game_view # Will give us access to all data

        # Variables that will hold sprite lists
        """ Set up the game and initialize the variables. """
        self.button_sprite = arcade.Sprite(BUTTON_IMAGE)
        self.button_sprite.center_x = self.left + (self.width // 2)
        self.button_sprite.center_y = self.height // 2
        self.button_sprite.scale = 1.0  # Default scale

        self.background_image = arcade.load_texture("assets/button_background.jpg")  # Load background image

        # Load the button click sound
        self.button_click_sound = arcade.load_sound(BUTTON_CLICK_SOUND)
        
        # Animation-related attributes
        self.scale_target = 1.0  # Target scale for animation
        self.scale_speed = 5.0  # Speed of scaling animation

        # Click tracker
        self.click_count = 0
        self.elapsed_time = 0
        self.clicks_per_sec = 0

    def on_draw(self):
         # Draw the background image
        arcade.draw_lrwh_rectangle_textured(self.left, self.bottom, self.width, self.height, self.background_image)
        
        # Draw button sprite
        self.button_sprite.draw()

        # Draw all the text containg the info 
        arcade.draw_text(f"{self.name}'s Button Factory", self.left, self.window.height - 60, 
            arcade.color.WHITE, 45, width=self.width, align="center", font_name="Jersey 15")
        arcade.draw_text(f"{self.game_view.score:.2f} Buttons", self.left, self.window.height // 2 + 200, 
            arcade.color.WHITE, 37.5, width=self.width, align="center", font_name="Jersey 15")
        arcade.draw_text(f"{self.calc_total_buttons_per_sec():.2f} buttons/s", self.left, self.window.height // 2 + 160, 
            arcade.color.WHITE, 30, width=self.width, align="center", font_name="Jersey 15")

        arcade.draw_text(f"Base Auto Value: {self.game_view.score_per_sec} buttons/s", self.left, self.window.height // 2 - 170, 
            arcade.color.WHITE, 30, width=self.width, align="center", font_name="Jersey 15")
        arcade.draw_text(f"Auto Multiplier: {self.game_view.score_per_sec_multi}", self.left, self.window.height // 2 - 220, 
            arcade.color.WHITE, 30, width=self.width, align="center", font_name="Jersey 15")
        arcade.draw_text(f"Base Click Value: {self.game_view.click_value}", self.left, self.window.height // 2 - 270, 
            arcade.color.WHITE, 30, width=self.width, align="center", font_name="Jersey 15")
        arcade.draw_text(f"Click Multiplier: {self.game_view.click_multi}", self.left, self.window.height // 2 - 320, 
            arcade.color.WHITE, 30, width=self.width, align="center", font_name="Jersey 15")
        
    def on_update(self, delta_time):
        # Increment score automatically based on score_per_sec
        self.game_view.score += self.game_view.score_per_sec * self.game_view.score_per_sec_multi * delta_time

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

        # Clicks per second calculation
        self.elapsed_time += delta_time
        if self.elapsed_time >= 1:  # Every second
            self.clicks_per_sec = self.click_count / self.elapsed_time # divides by elapsed time to ensure accuracy 
            self.click_count = 0 # Reset count to 0
            self.elapsed_time = 0 # Reset time trackter to 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.button_sprite.collides_with_point((x, y)):
            self.game_view.score += (self.game_view.click_value * self.game_view.click_multi)
            self.scale_target = 0.9  # Shrink the button when clicked
            self.click_count += 1
            # Play the click sound
            arcade.play_sound(self.button_click_sound)

    def calc_total_buttons_per_sec(self):
        auto = self.game_view.score_per_sec * self.game_view.score_per_sec_multi # calculate passive income
        manual = self.clicks_per_sec * self.game_view.click_value * self.game_view.click_multi # calculate active income made in a sec
        return auto + manual
