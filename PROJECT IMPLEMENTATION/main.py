from data_simulator import generate_market_data
from market_data_compression_agent import MarketDataCompressor, TradingAgent, generate_signals
from backtesting_engine import Backtester
from performance_metrics import evaluate_performance
from cost_analysis import api_cost_simulation
from sklearn.model_selection import train_test_split

data = generate_market_data()

compressor = MarketDataCompressor()
data = compressor.extract_features(data)
data = generate_signals(data)

features = data[["MA_10", "MA_30", "Volatility", "RSI"]]
compressed_features = compressor.compress(features)
labels = data["Signal"]

X_train, X_test, y_train, y_test = train_test_split(
    compressed_features, labels, test_size=0.2, shuffle=False
)

agent = TradingAgent(model_type="logistic")
agent.train(X_train, y_train)

signals = agent.predict(X_test)

backtester = Backtester()
portfolio = backtester.run(data["Close"].iloc[-len(signals):], signals)

metrics = evaluate_performance(portfolio)

cost_report = api_cost_simulation(
    raw_calls=500,
    compressed_calls=150
)

print("Performance Metrics:", metrics)
print("Cost Analysis:", cost_report)
