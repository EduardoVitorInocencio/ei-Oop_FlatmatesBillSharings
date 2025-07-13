class Bill:
    """
    Representa uma conta (ex: energia) com valor total e período.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Representa um morador que divide a conta proporcionalmente
    aos dias que ficou na casa.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return bill.amount * weight
