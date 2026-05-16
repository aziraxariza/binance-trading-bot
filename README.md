# Binance Futures Testnet Trading Bot

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

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input (argparse)
- Input validation
- Logging to file (bot.log)
- Error handling with fallback mock execution

## Note
Due to Binance Futures Testnet API access limitations,
a fallback mock execution system is implemented.
