import arcade

class StackableUpgrade:
    def __init__(self, base_cost, cost_multi, name, help_text):
        self.cost = base_cost # Base cost of upgrade
        self.cost_multi = cost_multi # Multiplier of cost of upgrade as more are bought
        self.active = False 
        self.name = name
        self.count = 0
        self.help_text = help_text

    def get_total_cost(self, amount):
        """Calculate the total cost for buying 'amount' upgrades."""
        total_cost = 0
        current_cost = self.cost # Check current cost
        for _ in range(amount): # For loop goes by amount
            total_cost += current_cost # Add current cost to increasing total cost
            current_cost *= self.cost_multi # Multi cost buy its multiplier
        return total_cost

    def can_afford(self, game_view, amount):
        """Check if the player has enough score to buy 'amount' upgrades."""
        return game_view.score >= self.get_total_cost(amount)
        
    def activate(self, game_view, sound, amount=1):
        """Buy 'amount' upgrades."""
        if self.can_afford(game_view, amount): # If affordable
            arcade.play_sound(sound) # Play sound effect
            total_cost = self.get_total_cost(amount) # Get the total cost
            game_view.score -= total_cost # Deduct total cost from current score
            self.count += amount # Add quantity of upgrade by amount purchase
            self.cost *= self.cost_multi ** amount # Multiply cost by the multiplier to the power of amount bought
            self.apply_effect(game_view, amount) # Applys upgrade effect
    
    def apply_effect(self, game_view, amount):
        """Apply the upgrade effect."""
        pass

    def getDesc(self, amount):
        return f"{self.name} (x{self.count}) - Cost: {self.get_total_cost(amount)}" # Shows amount of upgrade bought and it's cost

    def getColor(self):
        return arcade.color.BLACK # Color will always be black
    
    def getFullHelpText(self):
        return self.name + ": " + self.help_text # Return help text 

class FactoryWorker(StackableUpgrade):
    def __init__(self):
        super().__init__(100, 1.5, "Factory Workers", "Hires a factory worker to press 1 button/sec")

    def apply_effect(self, game_view, amount):
        game_view.score_per_sec += 1 * amount # Each worker adds 1 button/sec

class ButtonMachine(StackableUpgrade):
    def __init__(self):
        super().__init__(300, 1.6, "Button Machine", "Makes a machine that presses 3 buttons/sec")
    
    def apply_effect(self, game_view, amount):
        game_view.score_per_sec += 3 * amount # Each machine adds 3 buttons/sec

class PowerGenerator(StackableUpgrade):
    def __init__(self):
        super().__init__(500, 1.7, "Power Generator", "Creates a power generator that generates 5 buttons/sec")
    
    def apply_effect(self, game_view, amount):
        game_view.score_per_sec += 5 * amount # Each machine adds 5 buttons/sec

class ButtonBoss(StackableUpgrade):
    def __init__(self):
        super().__init__(1500, 1.8, "Button Boss", "Hires a button boss that generates 10 buttons/sec")
    
    def apply_effect(self, game_view, amount):
        game_view.score_per_sec += 10 * amount # Each machine adds 10 buttons/sec

class ButtonFactory(StackableUpgrade):
    def __init__(self):
        super().__init__(2000, 1.9, "Button Factory", "Creates a button factory that generates 15 buttons/sec")
    
    def apply_effect(self, game_view, amount):
        game_view.score_per_sec += 15 * amount # Each factory adds 15 buttons/sec

class ButtonBashMilk(StackableUpgrade):
    def __init__(self):
        super().__init__(200, 1.5, "Button Bash Milk", "Consume some Button Bash Milk that adds a button per click")
    
    def apply_effect(self, game_view, amount):
        game_view.click_value += 1 * amount # Drinking milk adds 1 button/click