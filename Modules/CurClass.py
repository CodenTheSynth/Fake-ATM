class Currency:
    def __init__(self, dollarworth, curamount, name):
        self.dollarworth = dollarworth
        self.curamount = curamount
        self.name = name
    
    def ConvertFromDollar(self, amount):
        return amount * self.dollarworth
    
    def ConvertToDollar(self, amount):
         return amount / self.dollarworth
    