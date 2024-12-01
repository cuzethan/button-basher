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
    
    def getHelpText(self):
        return self.help_text

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
        super().__init__(2000, "ButtonBooster", "Gain a considerable increase of buttons generated per sec")

    def apply_effect(self, game_view):
        game_view.score_per_sec_multi *= 2 #multiply point per sec by 2

class TurboClicker(SingleUpgrade): #temporary upgrade
    def __init__(self):
        super().__init__(250, "TurboClicker", "Temporary incease")

    def apply_effect(self, game_view):
        start_time = time.time()
        game_view.click_multi *= 2  #multiply click multi by 2 for 30 sec
        while time.time() - start_time < 30: #wait 30 sec
            pass
        game_view.click_multi /= 2 #revert to default multi
        self.active = False

class MaxClicker(SingleUpgrade): #temporary upgrade
    def __init__(self):
        super().__init__(5000, "Max Clicker", "Temporary increase")

    def apply_effect(self, game_view):
        start_time = time.time()
        game_view.score_per_sec_multi *= 3  #multiply button per sec by x3
        while time.time() - start_time < 30: #wait 60 sec
            pass
        game_view.score_per_sec_multi /= 3  #reset multi
        self.active = False