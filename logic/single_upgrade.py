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

    def activate(self, game_view, sound):
        if game_view.score >= self.cost and not self.active:
            game_view.score -= self.cost
            self.active = True
            arcade.play_sound(sound)
            self.apply_effect(game_view)
    
    def apply_effect(self, game_view):
        pass

class AutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(50, "AutoClicker")
    
    def apply_effect(self, game_view):
        game_view.score_per_sec += 1  # 1 point per second from AutoClicker

class DoubleClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(30, "DoubleClicker")

    def apply_effect(self, game_view):
        game_view.click_value = 2

class MegaAutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(500, "Mega Autoclicker")

    def apply_effect(self, game_view):
        game_view.score_per_sec += 5  # point per second from MegaAutoClicker

class ScoreMultiplier(SingleUpgrade):
    def __init__(self):
        super().__init__(500, "Score Multiplier")

    def apply_effect(self, game_view):
        game_view.click_multi += 0.5  #add click multiplier by 1.5
