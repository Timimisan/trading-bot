from bot.client import BinanceFuturesClient
from bot.validators import validate_side, validate_quantity, validate_price


class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def market_order(self, symbol: str, side: str, quantity: float):
        side = validate_side(side)
        quantity = validate_quantity(quantity)

        return self.client.place_market_order(symbol, side, quantity)

    def limit_order(self, symbol: str, side: str, quantity: float, price: float):
        side = validate_side(side)
        quantity = validate_quantity(quantity)
        price = validate_price(price)

        return self.client.place_limit_order(symbol, side, quantity, price)