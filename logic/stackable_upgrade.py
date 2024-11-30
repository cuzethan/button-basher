import arcade

class StackableUpgrade:
    def __init__(self, base_cost, cost_multi, name):
        self.cost = base_cost
        self.cost_multi = cost_multi
        self.active = False
        self.name = name
        self.count = 0

    def getDesc(self):
        return f"{self.name} (x{self.count}) - Cost: {self.cost}"

    def getColor(self):
        return arcade.color.GREEN if self.active else arcade.color.DARK_GREEN

    def activate(self, game_view):
        pass

class FactoryWorker(StackableUpgrade):
    def __init__(self):
        super().__init__(100, 1.5, "Factory Workers")

    def activate(self, game_view):
        if game_view.score >= self.cost:
            game_view.score -= self.cost
            self.count += 1
            self.active = True
            self.cost = self.cost * self.cost_multi  # Increase cost
            game_view.score_per_sec += 5  # Each worker adds 5 buttons/sec

