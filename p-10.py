from flask import Flask, render_template, request
import heapq
from collections import namedtuple

# Define a named tuple for tree nodes
class Node:
    def __init__(self, frequency, character=None, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right

    # Define comparison operators for heapq
    def __lt__(self, other):
        return self.frequency < other.frequency


app = Flask(__name__)

def build_huffman_tree(characters, frequencies):
    # Create a list of nodes from characters and frequencies
    nodes = [Node(frequency, character) for character, frequency in zip(characters, frequencies)]
    heapq.heapify(nodes)  # Convert the list into a min-heap

    while len(nodes) > 1:
        # Remove two nodes with the lowest frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        # Create a new node with combined frequency
        merged_node = Node(left.frequency + right.frequency, None, left, right)
        heapq.heappush(nodes, merged_node)

    return nodes[0]  # Root of the Huffman Tree

def generate_huffman_codes(node, code, mapping):
    if node.character is not None:  # Leaf node
        mapping[node.character] = code
    else:
        generate_huffman_codes(node.left, code + '0', mapping)
        generate_huffman_codes(node.right, code + '1', mapping)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            characters = request.form["characters"].split()
            frequencies = list(map(float, request.form["frequencies"].split()))
            # Build Huffman tree
            huffman_tree = build_huffman_tree(characters, frequencies)
            # Generate Huffman codes
            huffman_mapping = {}
            generate_huffman_codes(huffman_tree, '', huffman_mapping)
            result = huffman_mapping
        except ValueError:
            result = {"error": "Please enter valid characters and frequencies."}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
