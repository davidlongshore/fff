class Car(object):
    def __init__(self, acount, ownersname, bank, amount_in_acount, amountneeded):
        
        self.acount=acount
        self.ownersname=ownersname
        self.bank=bank
        self.amount_in_acount=amount_in_acount
        self.amountneeded=amountneeded
        

    def amount_in(self):
        print( "\n\n you have '" + str(self.amount_in_acount) + "' in your acount at the moment.\n\n" )
    def add(self):
        print( "\n\nyou have added some money to your acount\n\n" )
    def withdraw(self):
        print( "\n\nyou have withdrawn some money\n\n")
obj1=Car( "first acount", "david", "idk, to many to tell", 0, 50 )
obj1.add()
obj1.amount_in()
obj1.withdraw()
