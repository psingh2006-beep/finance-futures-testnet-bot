import argparse

from bot.orders import place_order

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True,
    help="Trading pair symbol"
)

parser.add_argument(
    "--side",
    required=True,
    help="BUY or SELL"
)

parser.add_argument(
    "--type",
    required=True,
    help="MARKET or LIMIT"
)

parser.add_argument(
    "--quantity",
    type=float,
    required=True,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Price for LIMIT order"
)

args = parser.parse_args()

try:

    validate_side(args.side)

    validate_order_type(args.type)

    validate_quantity(args.quantity)

    validate_price(
        args.price,
        args.type
    )

    print("\nORDER REQUEST")
    print("-" * 30)

    print(f"Symbol      : {args.symbol}")
    print(f"Side        : {args.side}")
    print(f"Order Type  : {args.type}")
    print(f"Quantity    : {args.quantity}")

    if args.price:
        print(f"Price       : {args.price}")

    response = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\nORDER SUCCESS")
    print("-" * 30)

    print(
        f"Order ID    : "
        f"{response.get('orderId')}"
    )

    print(
        f"Status      : "
        f"{response.get('status')}"
    )

    print(
        f"ExecutedQty : "
        f"{response.get('executedQty')}"
    )

    print(
        f"Avg Price   : "
        f"{response.get('avgPrice')}"
    )

except Exception as error:

    print("\nORDER FAILED")
    print("-" * 30)

    print(f"Error: {str(error)}")