from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)

def find_closest_to_zero_pair(arr):
    closest_sum = float('inf')
    closest_pairs = []

    # Generate all pairs manually
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pair_sum = arr[i] + arr[j]
            if abs(pair_sum) < abs(closest_sum):
                closest_sum = pair_sum
                closest_pairs = [(arr[i], arr[j])]
            elif abs(pair_sum) == abs(closest_sum):
                closest_pairs.append((arr[i], arr[j]))

    return closest_pairs

@app.route('/', methods=['GET', 'POST'])
def index():
    closest_pairs = []
    if request.method == 'POST':
        input_str = request.form['numbers']
        try:
            numbers = list(map(int, input_str.split(',')))
            closest_pairs = find_closest_to_zero_pair(numbers)
        except ValueError:
            closest_pairs = [('Error', 'Invalid input')]

    # Render HTML directly from the file
    return render_template_string(open('p2.html').read(), closest_pairs=closest_pairs)

if __name__ == "__main__":
    app.run(debug=True)
