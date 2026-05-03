from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "bank_secret_key_2026"

class BankAccount:
    def __init__(self, account_holder, account_no, account_type, balance=10000):
        self.account_holder = account_holder
        self.account_no = account_no
        self.account_type = account_type
        self.balance = balance
        self.pin = "1234"
        self.history = []
        self.bank_name = "SBI"
        self.branch = "Chennai"
        self.ifsc = "SBI0001006"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({
                "type": "Deposit",
                "amount": amount,
                "balance": self.balance,
                "time": timestamp
            })
            return True, f"Deposited Rs.{amount} successfully"
        return False, "Invalid amount"

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({
                "type": "Withdraw",
                "amount": amount,
                "balance": self.balance,
                "time": timestamp
            })
            return True, f"Withdrawn Rs.{amount} successfully"
        elif amount <= 0:
            return False, "Invalid amount"
        else:
            return False, "Insufficient balance"

    def verify_pin(self, pin):
        return pin == self.pin

account = BankAccount("Sathish Kumar", "1234567890", "Savings Account")

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    pin = request.form.get("pin")
    if account.verify_pin(pin):
        session["logged_in"] = True
        return redirect("/dashboard")
    else:
        return render_template("login.html", error="Invalid PIN")

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template("dashboard.html", account=account)

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if not session.get("logged_in"):
        return redirect("/")
    
    message = None
    if request.method == "POST":
        try:
            amount = int(request.form.get("amount"))
            success, msg = account.deposit(amount)
            message = msg
            if success:
                return redirect("/dashboard")
        except:
            message = "Invalid amount entered"
    
    return render_template("deposit.html", message=message)

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if not session.get("logged_in"):
        return redirect("/")
    
    message = None
    if request.method == "POST":
        try:
            amount = int(request.form.get("amount"))
            success, msg = account.withdraw(amount)
            message = msg
            if success:
                return redirect("/dashboard")
        except:
            message = "Invalid amount entered"
    
    return render_template("withdraw.html", message=message, balance=account.balance)

@app.route("/balance")
def balance():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template("balance.html", balance=account.balance)

@app.route("/history")
def history():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template("history.html", history=account.history)

@app.route("/account-details")
def account_details():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template("account_details.html", account=account)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)