import arcade

class SingleUpgrade:
    def __init__(self, cost, name):
        self.cost = cost
        self.active = False
        self.name = name

    def getDesc(self):
        if self.active:
            return self.name + " Activated"
        else:
            return self.name + " - Cost: " + str(self.cost)

    def getColor(self):
        return arcade.color.GREEN if self.active else arcade.color.DARK_GREEN

    def apply(self, game_view):
        pass

class AutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(50, "AutoClicker")

    def apply(self, game_view):
        """Adds 1 point to the score every second."""
        if self.active:
            game_view.score += 1


class DoubleClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(30, "DoubleClicker")

    def apply(self, game_view):
        """Doubles the score added per click when active."""
        if self.active:
            game_view.click_value = 2  # Sets each click to add 2 points
