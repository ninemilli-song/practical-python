# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table heading.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """
    def headings(self, headers):
        html_header = ''
        for h in headers:
            html_header += f'<th>{h}</th>'
        html_header = f'<tr>{html_header}</tr>'
        print(html_header)
        print()

    def row(self, rowdata):
        html_row = ''
        for row in rowdata:
            html_row += f'<td>{row}</td>'
        html_row = f'<tr>{html_row}</tr>'
        print(html_row)
        print()


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')


def print_table(portfolios, columns, fmt):
    fmt.headings(columns)
    for s in portfolios:
        fmt.row([str(getattr(s, colname)) for colname in columns])


