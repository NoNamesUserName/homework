class Account(object):
    num_accts=0
    def __init__(self, acct_name, balance, acct_no, acct_type):
        print("Welcome "+acct_name+"\n")
        print("------------------------------------------")
        self.acct_name = acct_name
        balance=0
        self.__balance = balance
        self.acct_no = acct_no
        self.acct_type = acct_type
        num_accts+=1
    def money_manage(self):
        
        print("\n Your Balance is $",self.balance ,".\n")
        print("------------------------------------------")
        depo= input("How much would \n you like to deposit")
        if depo>=0:
            ballance=balance+depo
            print("------------------------------------------")
            print"Your new balance is: $",self.balance,"\n"
        else:
            print("------------------------------------------")
            print("Error:\n Tried to withdraw funds in deposit")
            print("------------------------------------------")
    def __withdraw(self):
        print("------------------------------------------")
        print("\n Your Balance is $", self.balance ,".\n")
        print("------------------------------------------")
        withd= input("How much would \n you like to withdraw")
        if withd>=0 and balance-withd>=0:
            ballance=balance-withd
        else:
            print("------------------------------------------")
            print("Error:\n insufficient funds, you only have $"+ballance+".\n")
            print("------------------------------------------")
    def info(self):
        print("\nAcc:",self.acct_name,"\nBal: $",self.balance,"\nAcc#:",self.acct_no,"\nAcc type",self.acct_type,"\n") 

# main
acctname=input("What is your account name: ")
acctno=input("What is your acount number: ")
accttype=input("What type of account do you want type r for regular and s for student ")
acc=Account(acct_name=acctname, acct_no=acctno, acct_type=accttype)
acc.money_manage(self)
acc.info()

input("\n\nPress the enter key to exit.")







@balance.setter

