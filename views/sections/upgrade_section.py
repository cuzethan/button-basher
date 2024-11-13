import arcade

class UpgradeSection(arcade.Section):
    def __init__(self, left: int, bottom: int, width: int, height: int, game_view, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.game_view = game_view

        # Upgrade costs and activation status
        self.auto_clicker_cost = 50
        self.double_clicker_cost = 30
        self.auto_clicker_active = False
        self.double_clicker_active = False

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.ORANGE)
        arcade.draw_text("Upgrades", self.left, self.window.height - 60, 
                         arcade.color.BLACK, 25, width=self.width, align="center")

        # AutoClicker Upgrade
        auto_clicker_text = "AutoClicker - Cost: 50" if not self.auto_clicker_active else "AutoClicker Activated"
        auto_clicker_color = arcade.color.DARK_GREEN if not self.auto_clicker_active else arcade.color.GREEN
        arcade.draw_text(auto_clicker_text, self.left + 20, self.top - 100, auto_clicker_color, 16)

        # DoubleClicker Upgrade
        double_clicker_text = "DoubleClicker - Cost: 30" if not self.double_clicker_active else "DoubleClicker Activated"
        double_clicker_color = arcade.color.DARK_GREEN if not self.double_clicker_active else arcade.color.GREEN
        arcade.draw_text(double_clicker_text, self.left + 20, self.top - 140, double_clicker_color, 16)

    def on_mouse_press(self, x, y, button, modifiers):
        # Check for AutoClicker purchase
        if (self.left + 20 < x < self.left + 180 and self.top - 110 < y < self.top - 90):
            if self.game_view.button_section.score >= self.auto_clicker_cost and not self.auto_clicker_active:
                # Deduct cost and activate AutoClicker
                self.game_view.button_section.score -= self.auto_clicker_cost
                self.auto_clicker_active = True
                self.game_view.button_section.score_per_sec += 1  # 1 point per second from AutoClicker

        # Check for DoubleClicker purchase
        if (self.left + 20 < x < self.left + 180 and self.top - 150 < y < self.top - 130):
            if self.game_view.button_section.score >= self.double_clicker_cost and not self.double_clicker_active:
                # Deduct cost and activate DoubleClicker
                self.game_view.button_section.score -= self.double_clicker_cost
                self.double_clicker_active = True
                self.game_view.button_section.click_value = 2  # Sets each click to add 2 points

