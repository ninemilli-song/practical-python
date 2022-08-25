#
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, num):
        if self.shares >= num:
            self.shares = self.shares - num
        else:
            raise ValueError(f'The shares of sells out of shares range {self.shares}')