class AutoClicker:
    def __init__(self):
        self.cost = 50  # Cost for buying the autoclicker
        self.active = False

    def apply(self, game_view):
        """Adds 1 point to the score every second."""
        if self.active:
            game_view.score += 1


class DoubleClicker:
    def __init__(self):
        self.cost = 30  # Cost for buying double clicker
        self.active = False

    def apply(self, game_view):
        """Doubles the score added per click when active."""
        if self.active:
            game_view.click_value = 2  # Sets each click to add 2 points
        else:
            game_view.click_value = 1  # Revert to default click value
