import arcade

class StackableUpgrade:
    def __init__(self, base_cost, cost_multi, name):
        self.cost = base_cost
        self.cost_multi = cost_multi
        self.active = False 
        self.name = name
        self.count = 0

    def get_total_cost(self, amount):
        """Calculate the total cost for buying 'amount' upgrades."""
        total_cost = 0
        current_cost = self.cost
        for _ in range(amount):
            total_cost += current_cost
            current_cost *= self.cost_multi
        return total_cost

    def can_afford(self, game_view, amount):
        """Check if the player has enough score to buy 'amount' upgrades."""
        return game_view.score >= self.get_total_cost(amount)
        
    def activate(self, game_view, amount=1):
        """Buy 'amount' upgrades."""
        if self.can_afford(game_view, amount):
            total_cost = self.get_total_cost(amount)
            game_view.score -= total_cost
            self.count += amount
            self.cost *= self.cost_multi ** amount
            self.apply_effect(game_view, amount)    
    
    def apply_effect(self, game_view, amount):
        """Apply the upgrade effect."""
        pass

    def getDesc(self, amount):
        return f"{self.name} (x{self.count}) - Cost: {self.get_total_cost(amount)}"

    def getColor(self):
        return arcade.color.DARK_GREEN

class FactoryWorker(StackableUpgrade):
    def __init__(self):
        super().__init__(100, 1.5, "Factory Workers")

    def apply_effect(self, game_view, amount):
        game_view.score_per_sec += 5 * amount # Each worker adds 5 buttons/sec

