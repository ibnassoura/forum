def withdraw(balance,value):
    print "Current balance = "+str(balance)
    request=value
    if request<=balance and request>0:
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
        print "Sorry, we dont have enogh money or you entered a wront number"
        return balance 
    return balance - value


balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
