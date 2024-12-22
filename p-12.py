from flask import Flask, render_template, request
import itertools

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        # Get the number of nodes (cities)
        nodes = int(request.form['nodes'])

        # Initialize the distance matrix (input data)
        matrix = []
        for i in range(nodes):
            row = []
            for j in range(nodes):
                key = f"weight_{i}_{j}"
                weight_value = request.form.get(key, "∞")  # Handle missing keys
                row.append(weight_value if weight_value != "∞" else float('inf'))  # Default to inf if missing
            matrix.append(row)

        # Solve the TSP (for now, we'll just simulate a simple path for demonstration)
        path, cost, segments = solve_tsp(matrix)

        output = {
            'input_matrix': matrix,
            'path': path,
            'cost': cost,
            'segments': segments
        }

    return render_template("index.html", output=output)

def solve_tsp(matrix):
    # A simple TSP solver implementation (this is just a placeholder, you can implement the real TSP logic here)
    nodes = len(matrix)
    # Generate all possible permutations of cities
    all_permutations = itertools.permutations(range(nodes))
    min_cost = float('inf')
    best_path = None
    path_segments = []

    # Check each possible path and calculate the cost
    for perm in all_permutations:
        current_cost = 0
        segments = []
        for i in range(nodes - 1):
            current_cost += matrix[perm[i]][perm[i + 1]]
            segments.append(f"City {perm[i] + 1} -> City {perm[i + 1] + 1} = {matrix[perm[i]][perm[i + 1]]}")
        current_cost += matrix[perm[-1]][perm[0]]  # Add the cost to return to the starting city
        segments.append(f"City {perm[-1] + 1} -> City {perm[0] + 1} = {matrix[perm[-1]][perm[0]]}")

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = perm
            path_segments = segments

    # Convert best path from indices to city numbers (1-indexed)
    best_path = " -> ".join([f"City {x + 1}" for x in best_path])
    return best_path, min_cost, ", ".join(path_segments)

if __name__ == "__main__":
    app.run(debug=True)
