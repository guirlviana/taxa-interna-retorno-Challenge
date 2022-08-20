import numpy_financial as npf

class Cashflow():
    def __init__(self, initial_cashflow: dict = {}) -> None:
        self.cashflow = initial_cashflow

    def add_installment(self, amount: float, date: str): 
        if self.already_has_a_movement(date):
            self.cashflow[date] += (amount)
            return

        self.cashflow[date] = amount

    def add_investment(self, amount: float, date: str):
        amount = amount * -1
        if self.already_has_a_movement(date):
            self.cashflow[date] += (amount)
            return

        self.cashflow[date] = amount

    def already_has_a_movement(self, date: str):
        if date in self.cashflow.keys():
            return True
        return False
    
    def get_tir(self, by_percentage=False):
        irr = round(npf.irr(list(self.cashflow.values())), 2)
        if not by_percentage:
            return irr
        return irr * 100