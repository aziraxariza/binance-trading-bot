import logging
from bot.client import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"REAL ORDER: {order}")
        return order, "REAL"

    except Exception as e:
        logging.error(f"API FAILED: {e}")

        # ✅ Fallback mock response
        mock_order = {
            "orderId": 999999,
            "status": "FILLED",
            "executedQty": quantity,
            "avgPrice": price if price else "MARKET_PRICE"
        }

        logging.info(f"MOCK ORDER: {mock_order}")
        return mock_order, "MOCK"