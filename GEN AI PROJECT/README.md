# Compressed Financial Trading Agent

## Overview

This project implements a cost-efficient trading system that compresses financial market data before making trading decisions.  
The goal is to reduce API usage, lower computational overhead, and improve decision speed while maintaining predictive performance.

The system transforms raw market prices into compact feature representations and generates Buy / Sell / Hold signals using machine learning models.

---

## System Architecture

Market API → Feature Extraction → Data Compression → Decision Model → Trading Signal → Backtesting → Performance Evaluation

### 1. Market Data
Raw closing prices are either fetched from an API (production scenario) or simulated for experimentation.

### 2. Feature Extraction
Technical indicators are computed:
- Moving Average (MA-10, MA-30)
- Volatility
- Relative Strength Index (RSI)

These features summarize market behavior and reduce dependence on raw price sequences.

### 3. Data Compression
Feature vectors are scaled and compressed using Principal Component Analysis (PCA).  
This reduces dimensionality and lowers storage and computational cost.

### 4. Decision Engine
A machine learning classifier is trained:
- Logistic Regression
- Random Forest

The model outputs:
- Buy
- Sell
- Hold

### 5. Backtesting Engine
Simulates portfolio performance using predicted trading signals.

### 6. Performance Metrics
Evaluates:
- Cumulative Return
- Sharpe Ratio
- Maximum Drawdown

### 7. Cost Optimization
Simulates reduction in API calls by storing compressed historical summaries instead of raw market data.

---

## Project Structure

project/
│
├── market_data_compression_agent.py
├── backtesting_engine.py
├── performance_metrics.py
├── cost_analysis.py
├── data_simulator.py
├── main.py
├── requirements.txt
└── README.md
---

## Key Contributions

- Feature-level financial data summarization
- Dimensionality reduction before inference
- Modular trading pipeline design
- Strategy backtesting framework
- API cost reduction modeling

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Running the Project

Execute:

python main.py

This will:
- Generate market data
- Train the trading model
- Produce trading signals
- Backtest strategy performance
- Output cost analysis

---

## Limitations

- Uses simulated data for demonstration
- Not production-grade execution
- Simplified transaction logic (no slippage or transaction cost modeling)

---

## Future Improvements

- Real-time API integration
- Transaction cost modeling
- Hyperparameter optimization
- Deep learning-based compression
- Reinforcement learning trading strategy

---

## Conclusion

This project demonstrates how financial data compression combined with machine learning can create a more computationally efficient trading pipeline while maintaining structured decision-making capability.
