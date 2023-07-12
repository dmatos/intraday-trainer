# coding=utf-8

TICKERS_INPUT = 'config/tickers.csv'

if __name__ == '__main__':
    with open(TICKERS_INPUT) as tickers:
        for row in tickers:
            print(row)
