import random

class Currency_Roulette_Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.usd_to_ils_rate = None

    def get_money_interval(self, usd_amount):
        self.usd_to_ils_rate = self.get_current_usd_to_ils_rate()
        total_value = usd_amount * self.usd_to_ils_rate

        margin = 5 - self.difficulty
        interval = (total_value - margin, total_value + margin)
        return interval

    def get_current_usd_to_ils_rate(self):
        # For simplicity, this is a static rate
        return 3.7
