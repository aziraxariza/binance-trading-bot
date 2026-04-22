from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET")
    )

    # FORCE Binance Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client