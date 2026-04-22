import argparse
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
parser.add_argument("--price", type=float, help="Required for LIMIT orders")

args = parser.parse_args()

try:
    # ✅ Validate inputs
    validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

    # 📊 Print request
    print("\n📊 Order Request:")
    for key, value in vars(args).items():
        print(f"{key.upper()}: {value}")

    # 🚀 Place order (FIXED: unpack tuple)
    order, mode = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    # ⚡ Show execution mode
    print(f"\n⚡ Execution Mode: {mode}")

    # ✅ Print result safely
    print("\n✅ Order Result:")
    print(f"Order ID     : {order.get('orderId', 'N/A')}")
    print(f"Status       : {order.get('status', 'N/A')}")
    print(f"Executed Qty : {order.get('executedQty', 'N/A')}")
    print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")

except ValueError as ve:
    print(f"\n❌ Validation Error: {ve}")

except Exception as e:
    print(f"\n❌ Unexpected Error: {e}")