# report.py
#
# Exercise 2.4
import sys
import fileparse
from stock import Stock
import tableformat
from portfolio import Portfolio
import logging

def read_portfolio(filename, **opts):
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file,
                                        select=['name', 'shares', 'price'],
                                        types=[str, int, float],
                                        has_headers=True, **opts)

        portfolio = [Stock(**d) for d in portdicts]
        return Portfolio(portfolio)


def read_price(filename):
    with open(filename) as file:
        price_list = fileparse.parse_csv(file, types=[str, float], has_headers=False)
        prices = dict(price_list)
        return prices


# # Exercise 2.7
# portfolio = read_portfolio('Data/portfoliodate.csv')
# prices = read_price('Data/prices.csv')

# result = []
# for stock in portfolio:
#     name = stock['name']
#     price = float(stock['price'])
#     shares = int(stock['shares'])
#
#     current_price = float(prices[name])
#     gain_lose = round((current_price - price) * shares, 2)
#     result.append({
#         'name': name,
#         'shares': shares,
#         'price': price,
#         'current_price': current_price,
#         'change': gain_lose
#     })


# Exercise 2.9
def mark_report(portfolio, prices):
    result = []
    for stock in portfolio:
        name = stock.name
        price = float(stock.price)
        shares = int(stock.shares)

        current_price = float(prices[name])
        gain_lose = round((current_price - price) * shares, 2)
        result.append((name, shares, price, current_price, gain_lose))

    return result


def print_report(report, formatter):
    """
    output report
    """
    # headers = ('Name', 'Shares', 'Price', 'C_Price',  'Change')
    # print('%10s %10s %10s %10s %10s' % headers)
    # print(('-' * 10 + ' ') * len(headers))

    formatter.headings(['Name', 'Shares', 'Price', 'C_Price', 'Change'])
    # for r in report:
    #     print('%10s %10d %10.2f %10.2f %10.2f' % r)

    # Exercise 2.10
    for name, shares, price, c_price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{c_price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
    # for row in report:
    #     print('%10s %10d %10.2f %10.2f %10.2f' % row)


def portfolio_report(portfolio, prices, fmt='txt'):
    """
    portfolio - portfolio file path
    prices - prices file path
    """
    portfolio = read_portfolio(portfolio)
    prices = read_price(prices)

    report = mark_report(portfolio, prices)

    # print it out
    # formatter = tableformat.TextTableFormatter()
    # formatter = tableformat.CSVTableFormatter()
    # formatter = tableformat.HTMLTableFormatter()
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) < 3:
        raise SystemExit('Usage: %s portfolio pricefile' % args[0])

    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.WARNING,
    )
    main(sys.argv)


