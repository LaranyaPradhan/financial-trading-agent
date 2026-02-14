import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

class MarketDataCompressor:
    def __init__(self, n_components=3):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=n_components)

    def extract_features(self, df):
        df["MA_10"] = df["Close"].rolling(10).mean()
        df["MA_30"] = df["Close"].rolling(30).mean()
        df["Volatility"] = df["Close"].rolling(10).std()
        delta = df["Close"].diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = -delta.clip(upper=0).rolling(14).mean()
        rs = gain / loss
        df["RSI"] = 100 - (100 / (1 + rs))
        df = df.dropna()
        return df

    def compress(self, X):
        X_scaled = self.scaler.fit_transform(X)
        return self.pca.fit_transform(X_scaled)

class TradingAgent:
    def __init__(self, model_type="logistic"):
        if model_type == "logistic":
            model = LogisticRegression()
        else:
            model = RandomForestClassifier(n_estimators=100)

        self.pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("model", model)
        ])

    def train(self, X, y):
        self.pipeline.fit(X, y)

    def predict(self, X):
        preds = self.pipeline.predict(X)
        return ["Buy" if p == 1 else "Sell" if p == -1 else "Hold" for p in preds]

def generate_signals(df):
    df["Future_Return"] = df["Close"].pct_change().shift(-1)
    df["Signal"] = 0
    df.loc[df["Future_Return"] > 0.002, "Signal"] = 1
    df.loc[df["Future_Return"] < -0.002, "Signal"] = -1
    df = df.dropna()
    return df
