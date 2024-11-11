import arcade
from button_section import ButtonSection

class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        self.add_section(ButtonSection(self.window.width / 2, 0,
                                    self.window.width / 2, self.window.height,
                                    name='Button'))

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time):
        pass
