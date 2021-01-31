from flask import Flask, render_template,request, redirect
from cs50 import SQL
from models import db, User, Transactions
from sqlalchemy import exc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userbalances.db'
# Initialization of database
db.init_app(app)

@app.before_first_request
def initialize_database():
# with app.app_context():
    # db.create_all()
    try:
        db.create_all()
        user1 = User(username='test', checkingBalance=1.00, savingBalance=0.00, savingPercent=0.00)
        if not bool(User.query.filter_by(username='test').first()):
            db.session.add(user1)
            User.query.get("test").checkingBalance = 4.00
            db.session.commit()
    except exc.IntegrityError as e:
        errorInfo = e.orig.args
        print(errorInfo)
# Database schema is as shown
'''
    Table Name: transactions
    Columns: amount     date        type        savingPercent
    Datatype: Real   Integer     Integer        Real
    Explanation:
        Amount is stored as a real (floating point) number
        Date is stored as an integer representing the date & time in unix time (easier to convert it to local time if stored as unix epoch or utc?)
        Type is stored as an integer of 0 or 1 to represent boolean values (sqlite doesn't have native boolean data type) 0 means deposit & 1 means withdrawal
        savingPercent is stored as a real (floating point) number that should be between 0.1 & 1 (check this in logic)
'''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/checking', methods=["GET","POST"])
def checking():

    if request.method=="GET":
        checkBalance = User.query.get('test').checkingBalance
        return str(checkBalance)
        return render_template('checking.html')
    else:
        return redirect('/modifybalance')

@app.route('/savings', methods=["GET","POST"])
def savings():
    return "Savings Account Page"

@app.route('/transactions')
def transactions():
    return str(User.query.get('test'))

@app.route('/deposits')
def modifyDeposits():
    return render_template('deposits.html')

@app.route('/expenses')
def modifyExpenses():
    return render_template('expenses.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)