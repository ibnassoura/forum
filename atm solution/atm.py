class ATM:
    def __init__(self,balance,bank_name):
        self.balance=balance
        self.bankname=bank_name
        
    def withdraw(self,value):
        print "Welcome to "+str(self.bankname)
        print "Current balance = "+str(self.balance)
        request=value
        
        if request<=self.balance and request>0:
            moneylist=[100,50,10,5,2,1]
            for each in moneylist:
                while request%each<request:
                    print "Give "+str(each)
                    request=request-each
        else:
            print "Sorry, we dont have enogh money or you entered a wrong number"
            return self.balance
        balance=self.balance - value
        return balance


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
