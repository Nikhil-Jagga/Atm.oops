class ATM():
    def __init__(self,location,bankname,balance):
        
        self.location=location
        self.bankname=bankname
        self.balance=balance
        
    def deposit(self,):
        amount=int(input("enter the amount to deposit:"))
        if amount>0:
            self.balance+=amount
            print(f"your amount {amount}/- is credited and available balance is {self.balance}/- to {self.bankname} at {self.location} branch")
        else:
            print("invalid amount")
            
    def withdraw(self,):
        amount=int(input("enter the amount to be withdrawn:"))
        if amount<=self.balance:
           self.balance-=amount
           print(f"your amount {amount}/- is debited and available balance is {self.balance}/-")
        else:
            print("insufficient balance")
        
    def show_balance(self,):
        print(f"your current balance is:{self.balance}")

class ATM2(ATM):
    def mini_statement(self,):
        print("mini statement generated successfully...")


HDFC = ATM2("anantapur","hdfc",60000)


while True:
    print("\n---ATM MENU---")
    print("1.deposit")
    print("2.withdraw")
    print("3.show_balance")
    print("4.exit")
    print("5.mini statement")

    choice=int(input("enter your choice:"))

    if choice==1:
        HDFC.deposit()
    elif choice==2:
        HDFC.withdraw()
    elif choice==3:
        HDFC.show_balance()
    elif choice==4:
        print("Thank you for using ATM")
        break
    elif choice==5:
        HDFC.mini_statement()
    else:
        print("invalid choice")
