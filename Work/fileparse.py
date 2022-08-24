# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    # with open(filename) as f:
    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        if not has_headers:
            raise RuntimeError('select argument requires columns headers')
        indices = [headers.index(column) for column in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:
            continue
        # Filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rowno}: Couldn\'t convert {row}')
                    print(f'Reason {e}')

        # Make a dictionary
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
