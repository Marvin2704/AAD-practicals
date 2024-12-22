# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Function to calculate minimum coins
# def min_coins(value):
#     coins = [1, 4, 6]
#     dp = [float('inf')] * (value + 1)
#     dp[0] = 0  # Base case

#     for coin in coins:
#         for i in range(coin, value + 1):
#             dp[i] = min(dp[i], dp[i - coin] + 1)

#     return dp[value] if dp[value] != float('inf') else -1  # Return -1 if it's not possible

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     min_coins_result = None
#     if request.method == 'POST':
#         value = int(request.form['value'])
#         min_coins_result = min_coins(value)
    
#     return render_template('index.html', result=min_coins_result)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate minimum coins and track used coins
def min_coins(value):
    coins = [1, 4, 6]
    dp = [float('inf')] * (value + 1)
    dp[0] = 0  # Base case
    coin_used = [-1] * (value + 1)  # To track which coin was used

    for coin in coins:
        for i in range(coin, value + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[value] == float('inf'):
        return -1, []  # Return -1 if it's not possible, with an empty list

    # Backtrack to find the coins used
    result_coins = []
    while value > 0:
        coin = coin_used[value]
        result_coins.append(coin)
        value -= coin

    return dp[value], result_coins

@app.route('/', methods=['GET', 'POST'])
def index():
    min_coins_result = None
    coins_used = []
    if request.method == 'POST':
        value = int(request.form['value'])
        min_coins_result, coins_used = min_coins(value)
    
    return render_template('index.html', result=min_coins_result, coins_used=coins_used)

if __name__ == '__main__':
    app.run(debug=True)
