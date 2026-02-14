import numpy as np
import pandas as pd

def generate_market_data(n=500):
    np.random.seed(42)
    prices = np.cumsum(np.random.randn(n)) + 100
    return pd.DataFrame({"Close": prices})
