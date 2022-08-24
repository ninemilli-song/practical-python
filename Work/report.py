# report.py
#
# Exercise 2.4
import sys
import fileparse


def read_portfolio(filename):
    with open(filename) as file:
        portfolio = fileparse.parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True)
        return portfolio


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
        name = stock['name']
        price = float(stock['price'])
        shares = int(stock['shares'])

        current_price = float(prices[name])
        gain_lose = round((current_price - price) * shares, 2)
        result.append((name, shares, price, current_price, gain_lose))

    return result


def print_report(report):
    """
    output report
    """
    headers = ('Name', 'Shares', 'Price', 'C_Price',  'Change')
    print('%10s %10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    # for r in report:
    #     print('%10s %10d %10.2f %10.2f %10.2f' % r)

    # Exercise 2.10
    for row in report:
        print('%10s %10d %10.2f %10.2f %10.2f' % row)


def portfolio_report(portfolio, prices):
    """
    portfolio - portfolio file path
    prices - prices file path
    """
    portfolio = read_portfolio(portfolio)
    prices = read_price(prices)

    report = mark_report(portfolio, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfolio pricefile' % args[0])

    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    main(sys.argv)


