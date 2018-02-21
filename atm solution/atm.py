class ATM:
    def __init__(self,balance,bank_name):
        self.balance=balance
        self.bankname=bank_name
        
    def withdraw(self,value):
        print "Welcome to "+str(self.bankname)
        print "Current balance = "+str(self.balance)
        request=value
        
        if request<=self.balance and request>0:
            while request>0:
                if request%100<request:
                    print "give 100"
                    request=request-100
                elif request%50<request:
                    print "give 50"
                    request=request-50
                elif request%10<request:
                    print "give 10"
                    request=request-10
                elif request%5<request:
                    print "give 5"
                    request=request-5
                elif request%2<request:
                    print "give 2"
                    request=request-2
                else:
                    print "give 1"
                    request=request-1
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
