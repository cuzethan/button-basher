import arcade

# Constants
BUTTON_IMAGE = "assets/button.png"

class ButtonSection(arcade.Section):

    def __init__(self, left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        # Variables that will hold sprite lists
        """ Set up the game and initialize the variables. """
        self.button_sprite = arcade.Sprite(BUTTON_IMAGE)
        self.button_sprite.center_x = self.left + (self.width // 2)
        self.button_sprite.center_y = self.height // 2
        self.button_sprite.scale = 1.0  # Default scale

        # Animation-related attributes
        self.scale_target = 1.0  # Target scale for animation
        self.scale_speed = 5.0  # Speed of scaling animation

        # Set up the player info
        self.score = 0
        self.score_per_sec = 0

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.GRAY)
        self.button_sprite.draw()
        arcade.draw_text(f"{self.name}'s Button Factory", self.left, self.window.height - 60, 
            arcade.color.BLACK, 25, width=self.width, align="center")
        arcade.draw_text(f"{int(self.score)} Buttons", self.left, self.window.height // 2 + 200, 
            arcade.color.BLACK, 25, width=self.width, align="center")
        arcade.draw_text(f"{self.score_per_sec} Buttons Per Sec", self.left, self.window.height // 2 + 160, 
            arcade.color.BLACK, 20, width=self.width, align="center")
        
    def on_update(self, delta_time):
        # Increment score automatically based on score_per_sec
        self.score += self.score_per_sec * delta_time

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
            self.score += 1
            self.scale_target = 0.9  # Shrink the button when clicked
