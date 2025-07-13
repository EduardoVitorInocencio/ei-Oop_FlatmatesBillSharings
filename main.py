# %%
class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
    

class Flatmate:
    """
    Object that contains information about the person who lives in flat and pays a share of the bill.    
    
    """
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house  + flatmate2.days_in_house)
        self.self_amount = round(bill.amount * weight, 2)
        return self.self_amount
    

class PdfReport:
    """
    Creates a PDffile that contains data about the flamates sub as their names due amount and the periods of the bill
    
    """
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, bill):
        pass
    
# %%
the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.name, john.pays(bill=the_bill, flatmate2=marry))
print(marry.name, marry.pays(bill=the_bill, flatmate2=john))

# %%
