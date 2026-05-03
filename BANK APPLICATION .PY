
class bank:
    bank_name = "SBI"
    loc="chennai"
    ifsc_code= "SBI0001006"

    def __init__(self,name,acc_no,acc_pin,acc_type,balance=0):
        self.name=name
        self.__acc_no=acc_no
        self.__acc_pin=acc_pin
        self.acc_type=acc_type
        self.__balance=balance
        self.transaction_history= []
    
    
    #encapsulation
    def __deposite(self,ammount):
        self.__balance+=ammount
        self.transaction_history.append(f'deposite: Rs.{ammount}')
        print("deposite successfully")


    def __withdraw(self,ammount):
        if self.__balance>=ammount:
            self.__balance-=ammount
            self.transaction_history.append(f'withdraw: Rs.{ammount}')
            print("withdraw successfully")
            return True
        else:
            print("insufficient balance")
            return False
# authendication 

    def __authendicate(self):
        account=int(input("enter account number:"))
        pin=int(input("enter account pin:"))
        if self.__acc_no==account and self.__acc_pin==pin:
            print("authendication successful")
            return True
        
        else:
            print ("authendication failed")
            return False
 # last transaction
 # 
 # 
 # 
 #       
    def last_transaction(self):
        self.__generate_receipt()

# check balance

    def check_balance(self):
        if not self.__authendicate():
            return
       
        print(f'your account balance is {self.__balance}')

# deposite money

    def deposite_money(self):
        print("--------------deposite money----------------")
        if not self.__authendicate():
            return
        ammount=abs(int(input("enter ammount to deposite: Rs.")))
        self.__deposite(ammount)


# withdraw money

    def withdraw_money(self):

        print("--------------withdraw money----------------")
        if not self.__authendicate():
            return
        ammount=abs(int(input("enter ammount to withdraw: Rs.")))
        self.__withdraw(ammount)


 # generate recipt 

    def __generate_receipt(self):
        print("-------------- Generate Receipt ----------------")
        if self.__authendicate():
            print(f"Balance: Rs.{self.__balance}")

            print("\nTransaction History:")
            if not self.transaction_history:
                print("No transactions yet")
            else:
                for t in self.transaction_history:
                    print("-",t)



# display details

    def show_dt(self):
        print(f'name-------->{self.name}')
        print(f'bank name-------->{self.bank_name}')
        print(f'location-------->{self.loc}')
        print(f'IFSC code-------->{self.ifsc_code}')

        print(f'account number-------->{self.__acc_no}')
        
        print(f'account type-------->{self.acc_type}')
        print(f'account balance-------->{self.__balance}')


# variable and method calling

obj1=bank("sathish",1234567890,1234,"savings",10000)
obj1.show_dt()

obj1.deposite_money()
obj1.show_dt()
obj1.withdraw_money()
obj1.show_dt()
obj1.transaction_history()

