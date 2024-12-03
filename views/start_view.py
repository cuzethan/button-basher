import arcade
import pyglet
from views import NameInputView

class StartView(arcade.View):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Load the title image
        self.background_image = arcade.load_texture("assets/title_image.png") #Load the title image

        # Load the startup sound
        self.start_sound = arcade.load_sound("assets/game_sound.wav")
        self.sound_player = None

        # Import font
        pyglet.font.add_file("assets/font.ttf")


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

        # Draws Background
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background_image)

        #Draws "Start Game Button"
        arcade.draw_rectangle_filled(self.button_x, self.button_y, 
                                     self.button_width, self.button_height, 
                                     arcade.color.LIGHT_PINK)
        arcade.draw_rectangle_outline(self.button_x, self.button_y, 
                                     self.button_width, self.button_height, 
                                     arcade.color.BLACK, 4)
        arcade.draw_text("Start Game", self.button_x, self.button_y, 
                         arcade.color.BLACK, font_size=30, font_name="Jersey 15", anchor_x="center", anchor_y="center", bold = True)
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ Check if the button is clicked """
        if (self.button_x - self.button_width / 2 < x < self.button_x + self.button_width / 2 and
            self.button_y - self.button_height / 2 < y < self.button_y + self.button_height / 2):
            #Shows NameInput View if the button is clicked
            name_view = NameInputView(shared_sound=self.start_sound, sound_player=self.sound_player)
            self.window.show_view(name_view)