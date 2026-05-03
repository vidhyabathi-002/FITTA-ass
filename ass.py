
'''N, M = 3, 4
for _ in range(N):
    print("*" * M)'''
"""""
## calculator for user inputed numbers only addition 
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")""" 

class Bank:
    bankname = 'SBI'
    branch = 'chennai'
    ifsc = 123456789

    # customer method
    def customer(self, name, account_no, acc_type, balance, branch):
        self.name = name
        self.account_no = account_no
        self.acc_type = acc_type
        self.balance = balance
        self.branch = branch

    # check balance
    def check_balance(self):
        n = input("Enter yes or no to check balance: ")

        if n == "yes":
            print(f"Your balance is {self.balance}")

            if self.balance < 5000:
                print(" Your balance is low")

        else:
            print("Thank you for banking with us")




    def addmoney(self,balance):
        n=int(input("Enter the amount to add: "))
        self.balance+=n
        print(f"Your new balance is {self.balance}")




# object creation
s1 = Bank()

print(f"bankname: {s1.bankname}, branch: {s1.branch}, ifsc: {s1.ifsc}")

s1.customer('vidhya', 1111111, 'savings', 10000, 'chennai')

s1.check_balance()