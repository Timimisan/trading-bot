VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_side(side: str):
    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError(f"Invalid side: {side}. Use BUY or SELL")
    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type: {order_type}")
    return order_type


def validate_quantity(qty: float):
    if qty <= 0:
        raise ValueError("Quantity must be > 0")
    return float(qty)


def validate_price(price: float):
    if price <= 0:
        raise ValueError("Price must be > 0")
    return float(price)