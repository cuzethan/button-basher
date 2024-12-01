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

    def activate(self, game_view):
        return False #default behavior

class AutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(50, "AutoClicker")
    
    def activate(self, game_view):
        """Adds 1 point to the score every second."""
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            game_view.score_per_sec += 1  # 1 point per second from AutoClicker
            return True #activation successful. Sound plays
        return False #Not enough buying power. Sound doesn't play

class DoubleClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(30, "DoubleClicker")

    def activate(self, game_view):
        """Doubles the score added per click when active."""
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            game_view.click_value = 2  # Sets each click to add 2 points
            return True
        return False

class MegaAutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(500, "Mega Autoclicker")

    def activate(self, game_view):
        """Adds 10 points to the score every second"""
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            game_view.score_per_sec += 10  # 10 point per second from AutoClicker
            return True
        return False
