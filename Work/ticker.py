# ticker.py

from follow import follow
import csv
import report
from tableformat import create_formatter, print_table

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfile, logfile, fmt):
    columns = ['name', 'price', 'change']
    portfolio = report.read_portfolio('Data/portfolio.csv')
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, columns)
    portfolio_names = [getattr(s, 'name') for s in portfolio]
    rows = filter_symbols(rows, portfolio_names)

    formatter = create_formatter(fmt)
    formatter.headings(columns)
    for row in rows:
        formatter.row([str(val) for val in row.values()])

if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')

