from flask import Flask, render_template, request
import heapq

app = Flask(__name__)

# Dijkstra's algorithm to find shortest paths
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            if weight == float('inf'):
                continue  # Skip unconnected nodes
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    nodes = 0
    start_city = None
    graph = {}

    if request.method == "POST":
        nodes = int(request.form.get("nodes"))
        start_city = request.form.get("start_city").upper()

        # Gather city names
        cities = [request.form.get(f"city_{i}").upper() for i in range(nodes)]
        graph = {city: {} for city in cities}

        # Build graph with weights
        for i in range(nodes):
            for j in range(nodes):
                neighbor = cities[j]
                weight = request.form.get(f"weight_{i}_{j}")
                weight_value = float('inf') if weight == '∞' else int(weight)
                graph[cities[i]][neighbor] = weight_value

        # Run Dijkstra's algorithm
        result = dijkstra(graph, start_city)

        # Replace 'inf' with '∞' in results for clarity
        for city in result:
            result[city] = '∞' if result[city] == float('inf') else str(result[city])

    # Renderable graph for HTML visualization
    renderable_graph = {
        city: {neighbor: ('∞' if weight == float('inf') else str(weight)) for neighbor, weight in neighbors.items()}
        for city, neighbors in graph.items()
    }

    return render_template("index.html", result=result, nodes=nodes, start_city=start_city, graph=renderable_graph)

if __name__ == "__main__":
    app.run(debug=True)
