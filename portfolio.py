"""
Class that represents a portfolio
"""

import matplotlib.pyplot as plt

class Portfolio:
    """
    A class the models a portfolio and annual withdrawals between 2008 and the end of 2017.
    Uses historical returns on equities and bonds.
    """
    def __init__(self, starting_bal, withdrawal_rate, equity_allocation, rebalance):
        self.starting_bal = starting_bal
        self.withdrawal_rate = withdrawal_rate
        self.equity_allocation = equity_allocation
        self.bond_allocation = 1 - equity_allocation
        self.rebalance = rebalance

        self.current_bal = self.starting_bal
        self.equity_bal = self.current_bal * self.equity_allocation
        self.bond_bal = self.current_bal * self.bond_allocation

    @property
    def total_value(self):
        """
        Gets the total portfolio value
        :return: Float total value
        """
        return self.equity_bal + self.bond_bal

    @property
    def equity_withdrawal(self):
        """
        Gets equity withdrawal amount
        :return: Float withdrawal from equities
        """
        return self.equity_bal * self.withdrawal_rate

    @property
    def bond_withdrawal(self):
        """
        Gets bond withdrawal amount
        :return: Float withdrawal from bonds
        """
        return self.bond_bal * self.withdrawal_rate

    @property
    def current_year_withdrawal(self):
        """
        Gets total withdrawal for the year
        :return: Float total withdrawal
        """
        return self.equity_withdrawal + self.bond_withdrawal

    def calculate_portfolio(self, data):
        """
        Calculates yearly withdrawal and portfolio balance
        :param data: dictionary of yearly returns for equities and bonds
        :return: Lists: years, yearly equity balances, yearly bond balances
        """
        print(f'Starting num: {self.starting_bal}')
        print(f'Equity Allocation: {self.equity_allocation}')
        print(f'Bond Allocation: {round(self.bond_allocation, 2)}')
        print(f'Withdrawal Rate: {self.withdrawal_rate}')
        print(f'Rebalance: {self.rebalance}')

        # init with beginning values
        years = [2007]
        equity_balances = [self.equity_bal]
        bond_balances = [self.bond_bal]
        total_balances = [self.total_value]
        withdrawals = [0]
        # iter through years
        for year in data.keys():
            print(f'Annual withdrawal: {round(self.current_year_withdrawal, 2)}'.ljust(30, ' '), end='')
            withdrawals.append(float(self.current_year_withdrawal))
            # get new balances
            self.equity_bal -= self.equity_withdrawal
            self.bond_bal -= self.bond_withdrawal
            if self.rebalance:
                # rebalancing
                self.equity_bal = self.total_value * self.equity_allocation
                self.bond_bal = self.total_value - self.equity_bal
            # calculate new equity and bond values using the year's performance
            self.equity_bal *= float(data[year]['vtsax']) / 100 + 1
            self.bond_bal *= float(data[year]['vbtlx']) / 100 + 1
            # add balances to lists for matplot
            years.append(int(year))
            equity_balances.append(self.equity_bal)
            bond_balances.append(self.bond_bal)
            total_balances.append(self.equity_bal + self.bond_bal)

            print(f'{year} end total value: {round(self.total_value, 2)}')

        return years, equity_balances, bond_balances, total_balances, withdrawals

