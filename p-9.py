from flask import Flask, render_template, request

app = Flask(__name__)

# Class to represent each item with profit, weight, and profit-to-weight ratio
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.ratio = profit / weight

# Function to solve the fractional knapsack problem using the greedy algorithm
def fractional_knapsack(profits, weights, W):
    # Create a list of items
    items = [Item(profits[i], weights[i]) for i in range(len(profits))]
    
    # Sort items based on profit-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_profit = 0.0
    fractions = [0] * len(profits)
    
    for i in range(len(items)):
        if items[i].weight <= W:
            # Take the whole item
            fractions[i] = 1
            total_profit += items[i].profit
            W -= items[i].weight
        else:
            # Take fraction of the item
            fractions[i] = W / items[i].weight
            total_profit += items[i].profit * fractions[i]
            break

    return total_profit, fractions, items

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user input from form
    profits = list(map(int, request.form['profits'].strip().split(',')))
    weights = list(map(int, request.form['weights'].strip().split(',')))
    W = int(request.form['capacity'])
    
    # Solve the knapsack problem
    total_profit, fractions, items = fractional_knapsack(profits, weights, W)
    
    # Prepare data for display
    sorted_profits = [item.profit for item in items]
    sorted_weights = [item.weight for item in items]
    sorted_ratios = [item.ratio for item in items]

    return render_template(
        'index.html',
        total_profit=total_profit,
        fractions=fractions,
        sorted_profits=sorted_profits,
        sorted_weights=sorted_weights,
        sorted_ratios=sorted_ratios
    )

if __name__ == '__main__':
    app.run(debug=True)
