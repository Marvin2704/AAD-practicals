from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):  # l is the chain length
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def optimal_parenthesization(s, i, j):
    if i == j:
        return f"A{i + 1}"
    else:
        return f"({optimal_parenthesization(s, i, s[i][j])} x {optimal_parenthesization(s, s[i][j] + 1, j)})"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    dimensions = list(map(int, data['dimensions'].split(',')))
    m, s = matrix_chain_order(dimensions)
    result = {
        'min_multiplications': m[0][-1],
        'parenthesization': optimal_parenthesization(s, 0, len(dimensions) - 2)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
