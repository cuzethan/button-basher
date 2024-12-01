import arcade

class SingleUpgrade:
    def __init__(self, cost, name, help_text):
        self.cost = cost
        self.active = False
        self.name = name
        self.help_text = help_text

    def getDesc(self):
        if self.active:
            return self.name + " Activated"
        else:
            return self.name + " - Cost: " + str(self.cost)

    def getColor(self):
        return arcade.color.GREEN if self.active else arcade.color.DARK_GREEN

    def activate(self, game_view, sound):
        pass
    
    def getHelpText(self):
        return self.help_text

class AutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(50, "AutoClicker", "Gain an autoclicker which presses 1 button/second")
    
    def activate(self, game_view, sound):
        """Adds 1 point to the score every second."""
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            game_view.score_per_sec += 1  # 1 point per second from AutoClicker
            arcade.play_sound(sound)

class DoubleClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(30, "DoubleClicker", "Doubles your press value from 1 to 2.")

    def activate(self, game_view, sound):
        """Doubles the score added per click when active."""
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            game_view.click_value = 2  # Sets each click to add 2 points
            arcade.play_sound(sound)

class MegaAutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(500, "Mega Autoclicker", "Gain a mega autoclicker which presses 10 buttons/second")

    def activate(self, game_view, sound):
        """Adds 5 points to the score every second"""
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            game_view.score_per_sec += 5  # point per second from MegaAutoClicker
            arcade.play_sound(sound)

class ScoreMultiplier(SingleUpgrade):
    def __init__(self):
        super().__init__(500, "Score Multiplier")

    def activate(self, game_view, sound):
        """Increases the points gained per click by 1.5x."""
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            game_view.click_multi += 0.5  #add click multiplier by 1.5
            arcade.play_sound(sound)
