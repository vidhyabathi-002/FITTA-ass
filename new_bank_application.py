class Bank:
    bank_name = "SBI"
    loc = "Chennai"
    ifsc_code = "SBI0001006"

    def __init__(self, name, acc_no, acc_pin, acc_type, balance=0):
        self.name = name
        self.__acc_no = acc_no
        self.__acc_pin = acc_pin
        self.acc_type = acc_type
        self.__balance = balance
        self.transaction_history = []

    # Private deposit method
    def __deposit(self, amount):
        self.__balance += amount
        self.transaction_history.append(f"Deposit: Rs.{amount}")
        print("Deposit successful")

    # Private withdraw method
    def __withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.transaction_history.append(f"Withdraw: Rs.{amount}")
            print("Withdraw successful")
            return True
        else:
            print("Insufficient balance")
            return False

    # Private authentication
    def __authenticate(self):
        acc = int(input("Enter account number: "))
        pin = int(input("Enter PIN: "))

        if self.__acc_no == acc and self.__acc_pin == pin:
            print("Authentication successful")
            return True
        else:
            print("Authentication failed")
            return False

    # Check balance
    def check_balance(self):
        print("\nCheck Balance")
        if not self.__authenticate():
            return
        print(f" Current Balance: Rs.{self.__balance}")

    # Deposit money
    def deposit_money(self):
        print("\nDeposit Money")
        if not self.__authenticate():
            return
        amount = abs(int(input("Enter deposit amount: Rs.")))
        self.__deposit(amount)

    # Withdraw money
    def withdraw_money(self):
        print("\nWithdraw Money")
        if not self.__authenticate():
            return
        amount = abs(int(input("Enter Withdrawal amount: Rs.")))
        self.__withdraw(amount)

    # Generate receipt
    def generate_receipt(self):
        print("\nReceipt")
        print(f"Name: {self.name}")
        print(f"Balance: Rs.{self.__balance}")

        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions yet")
        else:
            for t in self.transaction_history:
                print("-", t)

        print("\nLast Transaction:")
        if not self.transaction_history:
            print("No transactions yet")
        else:
            print(self.transaction_history[-1])

    # Show details
    def show_details(self):
        print("\nAccount Details")
        print(f"Name: {self.name}")
        print(f"Bank: {self.bank_name}")
        print(f"Location: {self.loc}")
        print(f"IFSC: {self.ifsc_code}")
        print(f"Account No: {self.__acc_no}")
        print(f"Type: {self.acc_type}")
        print(f"Balance: Rs.{self.__balance}")

obj1 = Bank("Sathish", 1234, 1234, "Savings", 10000)


while True:

    print("\nWelcome to the Bank Application System Menu:")
    print("1. Show Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Generate Receipt")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ") 

    if choice == "1":
        obj1.show_details()
    elif choice == "2":
        obj1.deposit_money()
    elif choice == "3":
        obj1.withdraw_money()
    elif choice == "4":
        obj1.check_balance()    
    elif choice == "5":
        obj1.generate_receipt()
    elif choice == "6":
        print("Thank you for using the Bank Application System.")
        break
    else:
        print("Invalid choice. Please try again.")


