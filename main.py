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
        
    def pays(self, bill):
        pass
    

class PdfReport:
    """
    Creates a PDffile that contains data about the flamates sub as their names due amount and the periods of the bill
    
    """
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, bill):
        pass
