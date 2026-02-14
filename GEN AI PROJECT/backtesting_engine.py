class Backtester:
    def __init__(self, initial_capital=10000):
        self.initial_capital = initial_capital

    def run(self, prices, signals):
        capital = self.initial_capital
        position = 0
        portfolio_values = []

        for price, signal in zip(prices, signals):
            if signal == "Buy" and capital > 0:
                position = capital / price
                capital = 0
            elif signal == "Sell" and position > 0:
                capital = position * price
                position = 0

            portfolio_values.append(capital + position * price)

        return portfolio_values
