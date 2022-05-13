from decimal import Decimal


def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    # load prices
    prices = {}
    with open(prices_filename, "r", encoding="UTF-8") as f:
        for line in f:
            split = line.split(";")

            prices[split[0]] = Decimal(split[1].strip())

    # print(prices)

    bought = {}
    returned = {}
    paid = 0

    # load all kasse commands
    with open(cash_register_filename, "r", encoding="UTF-8") as f:
        for line in f:
            split = line.split(";")

            cmd = split[0]
            args = split[1].strip()

            if cmd == "buy":
                bought.setdefault(args, 0)
                bought[args] += 1
            elif cmd == "return":
                returned.setdefault(args, 0)
                returned[args] += 1
            elif cmd == "pay":
                paid += Decimal(args)

    # print(f"Bought: {bought}, returned {returned}, paid {paid}")
    # handle products

    cash_flow = []
    for item, amount in sorted(bought.items()):
        if item not in prices.keys():
            raise NoPrice()

        price = prices[item]

        cash_flow.append((amount, item, price * amount))

    for item, amount in sorted(returned.items()):
        if item not in prices.keys():
            raise NoPrice()

        price = prices[item]

        cash_flow.append((-1 * amount, item, -1 * price * amount))

    total = sum([x[2] for x in cash_flow])
    vat = total - (total / Decimal(1.25))

    to_return = total - paid

    if to_return > 0:
        raise NotEnoughPaid()

    return cash_flow, total, vat, paid, to_return


class NoPrice(Exception):
    pass


class NotEnoughPaid(Exception):
    pass


def receipt(prices_filename, cash_register_filename):
    """Construct a receipt of the cash register events,
    given the store prices."""

    # get receipt content from receipt_content()
    purcases_returns, total, vat, payment, change = receipt_content(
        prices_filename, cash_register_filename
    )

    # the formatted lines of the receipt
    receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]

    for nr, item, price in purcases_returns:
        receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")

    receipt_lines.append(f"Total: {total}")
    receipt_lines.append(f"Of which VAT: {vat:.2f}")
    receipt_lines.append(f"Payment: {payment}")
    receipt_lines.append(f"Change {change}")

    # add some dividers
    max_len = max(len(line) for line in receipt_lines)
    divider = "-" * max_len
    receipt_lines.insert(1, divider)
    receipt_lines.insert(-4, divider)
    receipt_lines.insert(-2, divider)

    return "\n".join(receipt_lines)
