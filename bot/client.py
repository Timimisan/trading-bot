import os
import json
import time
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
            raise ValueError("Missing BINANCE_API_KEY or BINANCE_API_SECRET")

        self.client = Client(api_key, api_secret)

        # IMPORTANT: correct Futures Testnet endpoint
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # -------------------------
    # INTERNAL HELPERS
    # -------------------------
    def _log_event(self, event: str, payload: dict):
        logger.info(json.dumps({"event": event, **payload}))

    def _log_error(self, event: str, error: Exception):
        logger.error(json.dumps({
            "event": event,
            "error": str(error),
            "type": type(error).__name__
        }), exc_info=True)

    # -------------------------
    # ACCOUNT
    # -------------------------
    def get_account(self):
        try:
            return self.client.futures_account()
        except (BinanceAPIException, BinanceRequestException) as e:
            self._log_error("ACCOUNT_FETCH_FAILED", e)
            raise RuntimeError("Account fetch failed")

    def check_balance(self):
        account = self.get_account()
        return account.get("totalWalletBalance")

    # -------------------------
    # MARKET ORDER
    # -------------------------
    def place_market_order(self, symbol: str, side: str, quantity: float):
        start = time.time()

        try:
            self._log_event("MARKET_ORDER_REQUEST", {
                "symbol": symbol,
                "side": side,
                "quantity": quantity
            })

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            latency = time.time() - start

            self._log_event("MARKET_ORDER_SUCCESS", {
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "latency_sec": round(latency, 4)
            })

            return order

        except (BinanceAPIException, BinanceRequestException) as e:
            self._log_error("MARKET_ORDER_FAILED", e)
            raise RuntimeError(str(e))

    # -------------------------
    # LIMIT ORDER
    # -------------------------
    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        start = time.time()

        try:
            self._log_event("LIMIT_ORDER_REQUEST", {
                "symbol": symbol,
                "side": side,
                "quantity": quantity,
                "price": price
            })

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )

            latency = time.time() - start

            self._log_event("LIMIT_ORDER_SUCCESS", {
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "latency_sec": round(latency, 4)
            })

            return order

        except (BinanceAPIException, BinanceRequestException) as e:
            self._log_error("LIMIT_ORDER_FAILED", e)
            raise RuntimeError(str(e))