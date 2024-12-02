import arcade
from views import NameInputView

class StartView(arcade.View):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        #Load the title image
        self.background_image = arcade.load_texture("assets/title_image.png") #Load the title image

        #Load the startup sound
        self.start_sound = arcade.load_sound("assets/game_sound.wav")
        self.sound_player = None


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

        # Play the start sound
        if not self.sound_player:
            self.sound_player = arcade.play_sound(self.start_sound, looping = True) 

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background_image)

        #arcade.draw_text("BUTTON BASHER", self.window.width / 2, self.window.height / 2,
        #                 arcade.color.WHITE, font_size=50, anchor_x="center")
        #arcade.draw_text("Click To Start Game", self.window.width / 2, self.window.height / 2 - 40,
        #                 arcade.color.WHITE, font_size=20, anchor_x="center")
        # Draw the button
        arcade.draw_rectangle_filled(self.button_x, self.button_y, 
                                     self.button_width, self.button_height, 
                                     arcade.color.LIGHT_PINK)
        arcade.draw_text("Start Game", self.button_x, self.button_y, 
                         arcade.color.BLACK, font_size=20, font_name= "assets/font.ttf", anchor_x="center", anchor_y="center", bold = True)

    def on_mouse_press(self, x, y, button, modifiers):
        """ Check if the button is clicked """
        if (self.button_x - self.button_width / 2 < x < self.button_x + self.button_width / 2 and
            self.button_y - self.button_height / 2 < y < self.button_y + self.button_height / 2):
            #Start the game if the button is clicked
            name_view = NameInputView(shared_sound=self.start_sound, sound_player=self.sound_player)
            self.window.show_view(name_view)