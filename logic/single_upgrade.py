import arcade
import time

class SingleUpgrade:
    def __init__(self, cost, name, help_text):
        self.cost = cost
        self.active = False
        self.name = name
        self.help_text = help_text

    def getDesc(self):
        if self.active:
            return self.name + " Activated" # Shows that upgrade is activate 
        else:
            return self.name + " - Cost: " + str(self.cost) # Default display for upgrade

    def getColor(self):
        return arcade.color.GREEN if self.active else arcade.color.BLACK # Turns font green if active, else shows black

    def activate(self, game_view, sound):
        if game_view.score >= self.cost and not self.active: # If enough money and not active
            game_view.score -= self.cost # Deduct cost from total score
            self.active = True # Set upgrade as active
            arcade.play_sound(sound) # Play purchase sound effect
            self.apply_effect(game_view) # Apply upgrade effect (different for every upgrade)
    
    def apply_effect(self, game_view):
        pass
    
    def getFullHelpText(self):
        return self.name + ": " + self.help_text # Returns info on upgrade

class AutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(50, "AutoClicker", "Gain an autoclicker which presses 1 button/second")
    
    def apply_effect(self, game_view):
        game_view.score_per_sec += 1  # 1 point per second from AutoClicker

class ButtonGear(SingleUpgrade):
    def __init__(self):
        super().__init__(30, "Button Gear", "Creates button gear that increase button click multi by 1.10")

    def apply_effect(self, game_view):
        game_view.click_multi *= 1.10

class MegaAutoClicker(SingleUpgrade):
    def __init__(self):
        super().__init__(500, "Mega Autoclicker", "Gain a mega autoclicker which increases button per sec by 1.5x")

    def apply_effect(self, game_view):
        game_view.score_per_sec_multi *= 1.5 # multi point per sec by 1.5

class ButtonEvolver(SingleUpgrade):
    def __init__(self):
        super().__init__(1000, "Button Evolver", "Evolve button to make click multiplier by 1.25x")

    def apply_effect(self, game_view):
        game_view.click_multi *= 1.25  #multiply click multiplier by 1.25

class ButtonBooster(SingleUpgrade):
    def __init__(self):
        super().__init__(2000, "ButtonBooster", "Boosts button mechanics which increases button per sec by 2x")

    def apply_effect(self, game_view):
        game_view.score_per_sec_multi *= 2 #multiply point per sec by 2