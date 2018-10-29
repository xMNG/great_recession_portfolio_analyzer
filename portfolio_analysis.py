#! python3
# portfolio_analysis.py - analyzes portfolio if you had retired at the start of 08
# Analyzer uses argparse if you want to rebalance, give starting numbers, equity allocation

import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from portfolio import Portfolio

# data scraped from vanguard
MARKET_DATA = {"2008": {"vtsax": "-37.04", "vbtlx": "5.24"},
               "2009": {"vtsax": "28.76", "vbtlx": "5.93"},
               "2010": {"vtsax": "17.28", "vbtlx": "6.58"},
               "2011": {"vtsax": "1.08", "vbtlx": "7.92"},
               "2012": {"vtsax": "16.44", "vbtlx": "4.32"},
               "2013": {"vtsax": "33.51", "vbtlx": "-1.97"},
               "2014": {"vtsax": "12.58", "vbtlx": "5.85"},
               "2015": {"vtsax": "0.40", "vbtlx": "0.44"},
               "2016": {"vtsax": "12.68", "vbtlx": "2.75"},
               "2017": {"vtsax": "21.19", "vbtlx": "3.63"}}


def percentage_in_decimal(num):
    """
    Function to validate input for floats between 0 and 1
    :param num: Float or int
    :return: Float
    """
    num = float(num)
    if num < 0.0 or num > 1.0:
        raise argparse.ArgumentTypeError(f"{num} not in range [0.0, 1.0].")
    return num


def positive_starting_bal(num):
    """
    Function to validate input for starting bal above 0
    :param num: Int number
    :return: Int num
    """
    num = int(num)
    if num <= 0:
        raise argparse.ArgumentTypeError(f'{num} not above 0.')
    return num


def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--sb', '--start_balance', type=positive_starting_bal, dest='starting_bal',
                        default=1000000, help='Enter an int starting balance.')
    parser.add_argument('--ea', '--equity_allocation', type=percentage_in_decimal, dest='equity_allocation',
                        default=1, help='Enter equity allocation.')
    parser.add_argument('--wr', '--withdrawal_rate', type=percentage_in_decimal, dest='withdrawal_rate',
                        default=.04, help='Enter withdrawal rate.')
    parser.add_argument('--rb', '--rebalance', action='store_true', dest='rebalance',
                        default=False, help='Enter whether to rebalance.')
    args = parser.parse_args()

    # instantiate Portfolio with parser arguments
    portfolio = Portfolio(args.starting_bal, args.withdrawal_rate, args.equity_allocation, args.rebalance)
    # call method to calculate
    years, equity_balances, bond_balances, total_balances, withdrawals = portfolio.calculate_portfolio(MARKET_DATA)


    # line plot
    ax = plt.subplot(2, 1, 1)
    # don't chart allocation if fully stocks
    if args.equity_allocation == 1:
        plt.plot(years, equity_balances, label='equities', marker='o')
    elif args.equity_allocation == 0:
        plt.plot(years, bond_balances, label='bonds', marker='o')
    else:
        plt.plot(years, equity_balances, label='equities', marker='o')
        plt.plot(years, bond_balances, label='bonds', marker='o')
        plt.plot(years, total_balances, label='total', marker='o')
    plt.title(f'Great Recession Portfolio Analyzer\n{format(args.starting_bal, ",")} starting balance, '
              f'{int(args.equity_allocation * 100)}:{int(100 - (args.equity_allocation * 100))} equity-bond allocation\n'
              f'Rebalance = {args.rebalance}')
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.legend()
    plt.ylabel('End of Year Value')
    plt.grid(b=True, which='both', axis='both')

    # bar chart
    ax2 = plt.subplot(2, 1, 2)
    plt.bar(years, withdrawals, width=0.5, label='withdrawals')
    plt.xlabel('Year')
    plt.ylabel('Withdrawals')
    plt.legend()

    ax2.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.grid(b=True, which='both', axis='y')
    plt.show()

    # TODO add grid
    # TODO make the y axis more detailed
    # TODO add coordinates for final values
    # TODO add withdrawals on second axes via barchart
    # TODO add better theme


if __name__ == '__main__':
    main()
