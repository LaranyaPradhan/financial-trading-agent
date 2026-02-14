import numpy as np

def evaluate_performance(portfolio_values):
    returns = np.diff(portfolio_values) / portfolio_values[:-1]
    cumulative_return = (portfolio_values[-1] / portfolio_values[0]) - 1
    sharpe_ratio = np.mean(returns) / np.std(returns) * np.sqrt(252)
    max_drawdown = np.min(
        portfolio_values / np.maximum.accumulate(portfolio_values) - 1
    )

    return {
        "Cumulative Return": cumulative_return,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown
    }
