def validate_side(side):

    valid_sides = ["BUY", "SELL"]

    if side not in valid_sides:
        raise ValueError(
            "Invalid side. Use BUY or SELL."
        )


def validate_order_type(order_type):

    valid_types = ["MARKET", "LIMIT"]

    if order_type not in valid_types:
        raise ValueError(
            "Invalid order type. Use MARKET or LIMIT."
        )


def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than 0."
        )


def validate_price(price, order_type):

    if order_type == "LIMIT":

        if price is None:
            raise ValueError(
                "LIMIT order requires price."
            )

        if price <= 0:
            raise ValueError(
                "Price must be greater than 0."
            )