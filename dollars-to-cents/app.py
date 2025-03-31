from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    coins = None
    if request.method == 'POST':
        try:
            dollars = float(request.form['dollars'])
            cents = int(round(dollars * 100))
            coins = calculate_coins(cents)
        except ValueError:
            coins = 'Invalid input. Please enter a valid dollar amount.'
    return render_template('index.html', coins=coins)

def calculate_coins(cents):
    coin_values = {'quarters': 25, 'dimes': 10, 'nickels': 5, 'pennies': 1}
    coin_count = {}
    for coin, value in coin_values.items():
        coin_count[coin], cents = divmod(cents, value)
    return coin_count

if __name__ == '__main__':
    app.run(debug=True)