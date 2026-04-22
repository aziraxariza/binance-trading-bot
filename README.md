# Binance Futures Testnet Trading Bot

## Setup
1. Clone repo
2. Install requirements:
   pip install -r requirements.txt

3. Add .env file with API keys

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Features
- Market & Limit Orders
- Input validation
- Logging (bot.log)
- Error handling

## Assumptions
- Testnet only
- USDT-M futures