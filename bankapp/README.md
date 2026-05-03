# SBI Bank Application

A full-featured web-based banking application built with Flask. This application demonstrates modern banking operations including deposits, withdrawals, balance checks, and transaction history.

## Features

code run command :


cd "C:\Users\VIDHYABATHI K\OneDrive\Desktop\FITA ass"; .\.venv\Scripts\Activate.ps1; cd bankapp; python app.py



- Login/Authentication: Secure PIN-based login system
- Dashboard: Main hub with quick access to all banking features
- Deposit Money: Add funds to your account
- Withdraw Money: Withdraw funds with balance validation
- Check Balance: View current account balance
- Transaction History: View all past transactions with timestamps
- Account Details: View complete account information including bank details
- Responsive Design: Mobile-friendly interface

## Project Structure

```
bankapp/
├── app.py                 # Flask application and routes
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── login.html
│   ├── dashboard.html
│   ├── deposit.html
│   ├── withdraw.html
│   ├── balance.html
│   ├── history.html
│   └── account_details.html
└── static/
    └── style.css         # Styling for all pages
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Steps

1. Navigate to the bankapp folder:

   ```
   cd "C:\Users\VIDHYABATHI K\OneDrive\Desktop\FITA ass\bankapp"
   ```
2. Install Flask (if not already installed):

   ```
   pip install Flask
   ```
3. Run the application:

   ```
   python app.py
   ```
4. Open in browser:

   - Go to: `http://localhost:5000`

## Default Login Credentials

- Account Holder: Sathish Kumar
- Account Number: 1234567890
- PIN: 1234
- Starting Balance: Rs. 10,000

## Features Explained

### Login Page

- Secure entry point with PIN authentication
- Demo credentials displayed for easy access

### Dashboard

- Welcome message with account holder name
- Current balance display
- Quick access buttons to all features
- Account summary table

### Deposit

- Enter amount to deposit
- Instantly updates account balance
- Records transaction in history

### Withdraw

- Enter amount to withdraw
- Validates sufficient balance
- Prevents overdrafts
- Records transaction in history

### Check Balance

- Display current account balance
- Shows balance information

### Transaction History

- Lists all deposits and withdrawals
- Shows transaction type, amount, and balance after transaction
- Includes timestamp for each transaction

### Account Details

- Complete account information
- Bank details (name, branch, IFSC)
- Current balance
- Account type and number

## Technical Details

### Built With

- Backend: Flask (Python web framework)
- Frontend: HTML5, CSS3, Jinja2 templates
- Session Management: Flask Sessions

### Security Features

- PIN-based authentication
- Session management for logged-in users
- Password-protected routes
- Input validation

## Usage Example

1. Launch the app and access http://localhost:5000
2. Login with PIN: 1234
3. View dashboard
4. Deposit money (e.g., Rs. 5000)
5. Check balance to confirm
6. View transaction history
7. Logout

## Future Enhancements

- Multiple account support
- User registration
- Database integration
- Advanced security (password hashing, 2FA)
- Fund transfers between accounts
- Email notifications
- Mobile app version

## Author

Created as a demonstration of object-oriented programming and web development concepts.

## License

Educational Use Only
