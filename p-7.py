from flask import Flask, render_template, request

app = Flask(__name__)

# Function to implement the Fractional Knapsack algorithm
def fractional_knapsack(values, weights, W):
    n = len(values)
    index = list(range(n))
    # Calculate value/weight ratio and sort items based on it
    ratio = [v / w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    
    max_value = 0
    fractions = [0] * n
    
    for i in index:
        if weights[i] <= W:
            max_value += values[i]
            W -= weights[i]
            fractions[i] = 1
        else:
            fractions[i] = W / weights[i]
            max_value += values[i] * fractions[i]
            break
    
    return max_value, fractions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user input from form
    values = list(map(int, request.form['values'].split(',')))
    weights = list(map(int, request.form['weights'].split(',')))
    W = int(request.form['capacity'])
    
    # Call the knapsack function
    max_value, fractions = fractional_knapsack(values, weights, W)
    
    return render_template('index.html', max_value=max_value, fractions=fractions, values=values, weights=weights)

if __name__ == '__main__':
    app.run(debug=True)
