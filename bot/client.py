import json
import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import setup_logger


logger = setup_logger()
load_dotenv()


class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("Missing API credentials in environment variables")

        # Create base client
        self.client = Client(api_key, api_secret)

        # IMPORTANT: point to Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_account(self):
        try:
            return self.client.futures_account()
        except (BinanceAPIException, BinanceRequestException):
            logger.error("Account fetch failed", exc_info=True)
            raise RuntimeError("Account fetch failed")

    def place_market_order(self, symbol: str, side: str, quantity: float):
        try:
            logger.info(json.dumps({
                "event": "MARKET_ORDER",
                "symbol": symbol,
                "side": side,
                "quantity": quantity
            }))

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(json.dumps({
                "event": "ORDER_SUCCESS",
                "orderId": order.get("orderId"),
                "status": order.get("status")
            }))
            return order

        except Exception as e:
            logger.error(json.dumps({
                "event": "ORDER_FAILED",
                "error": str(e)
            }))
            raise RuntimeError(str(e))

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        try:
            logger.info(json.dumps({
                "event": "MARKET_ORDER",
                "symbol": symbol,
                "side": side,
                "quantity": quantity
            }))

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )

            logger.info(json.dumps({
                "event": "ORDER_SUCCESS",
                "orderId": order.get("orderId"),
                "status": order.get("status")
            }))
            return order

        except Exception as e:
            logger.error(json.dumps({
                "event": "ORDER_FAILED",
                "error": str(e)
            }))
            raise RuntimeError(str(e))

    def check_balance(self):
        return self.client.futures_account()