# pcost.py
#
# Exercise 1.27
import sys
import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([stock.shares * stock.price for stock in portfolio])


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfolio' % args[0])

    cost = portfolio_cost(args[1])
    print(f'Total cost {cost}')

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else :
#     filename = 'Data/portfolio.csv'

if __name__ == '__main__':
    main(sys.argv)

