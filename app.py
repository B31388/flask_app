from flask import Flask, render_template, request, redirect, url_for
#from accounts import accounts, SavingsAccount, CheckingAccount
from models.account_types import accounts, SavingsAccount, CheckingAccount

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])

def create_account():
    if request.method == 'POST':
        acc_type = request.form['account_type']
        acc_num = request.form['account_number']
        if acc_num in accounts:
            return "Account already exists."
        if acc_type == 'savings':
            accounts[acc_num] = SavingsAccount(acc_num)
        elif acc_type == 'checking':
            accounts[acc_num] = CheckingAccount(acc_num)
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        acc_num = request.form['account_number']
        amount = float(request.form['amount'])
        if acc_num in accounts:
            accounts[acc_num].deposit(amount)
        return redirect(url_for('index'))
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        acc_num = request.form['account_number']
        amount = float(request.form['amount'])
        if acc_num in accounts:
            accounts[acc_num].withdraw(amount)
        return redirect(url_for('index'))
    return render_template('withdraw.html')

@app.route('/balance', methods=['GET', 'POST'])
def check_balance():
    balance = None
    if request.method == 'POST':
        acc_num = request.form['account_number']
        if acc_num in accounts:
            balance = accounts[acc_num].balance
    return render_template('balance.html', balance=balance)

#if __name__ == '__main__':
#    app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)