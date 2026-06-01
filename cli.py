import typer
from bot.orders import OrderService

app = typer.Typer()

service = OrderService()


@app.command()
def account():
    """Check futures account balance"""
    result = service.client.get_account()
    typer.echo(f"Balance: {result.get('totalWalletBalance')}")


@app.command()
def market(symbol: str, side: str, quantity: float):
    """Place MARKET order"""
    result = service.market_order(symbol, side, quantity)

    typer.echo("MARKET ORDER PLACED")
    typer.echo(f"Order ID: {result.get('orderId')}")
    typer.echo(f"Status: {result.get('status')}")
    typer.echo(f"Executed Qty: {result.get('executedQty')}")


@app.command()
def limit(symbol: str, side: str, quantity: float, price: float):
    """Place LIMIT order"""
    result = service.limit_order(symbol, side, quantity, price)

    typer.echo("LIMIT ORDER PLACED")
    typer.echo(f"Order ID: {result.get('orderId')}")
    typer.echo(f"Status: {result.get('status')}")


if __name__ == "__main__":
    app()