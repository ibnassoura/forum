class ATM:
    def __init__(self,balance,bank_name):
        self.balance=balance
        self.bankname=bank_name
        self.withdrawals_list = []
        
    def withdraw(self,request):
        print "Welcome to "+str(self.bankname)
        print "Current balance = "+str(self.balance)
        
        if request<=self.balance and request>0:
            self.balance=self.balance - request
            self.withdrawals_list.append(request)
            moneylist=[100,50,10,5,2,1]
            for each in moneylist:
                while request%each<request:
                    print "Give "+str(each)
                    request=request-each
        else:
            print "Sorry, we dont have enogh money or you entered a wrong number"
            return self.balance
        return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)

print "ATM 1 withdrawals: "
atm1.show_withdrawals()

print "ATM 2 withdrawals: "
atm2.show_withdrawals()

