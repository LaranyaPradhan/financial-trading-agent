# Project Documentation

## 1. Objective
To build a trading agent that compresses financial market data to reduce API cost and improve decision speed.

## 2. System Architecture
Market API → Data Compression → Pattern Extraction → Decision Engine → Trading Signal

## 3. Data Compression Strategy
- Feature extraction (moving average, RSI, volatility)
- Dimensionality reduction
- Store summarized vectors instead of raw data

## 4. Decision Model
- Logistic Regression / Random Forest
- Output: Buy / Sell / Hold

## 5. Cost Optimization
- Reduce number of API calls
- Store compressed historical summaries
- Faster inference time

## 6. Limitations
- Not production-grade
- Basic simulation environment

## 7. Conclusion
The system demonstrates efficient financial data processing with reduced computational and API cost.
