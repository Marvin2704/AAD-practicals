from flask import Flask, render_template, request

app = Flask(__name__)

# Function to find the longest common subsequence (LCS)
def longest_common_subsequence(P, Q):
    m = len(P)
    n = len(Q)

    # Create a 2D table to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if P[i - 1] == Q[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find one of the LCS
    i, j = m, n
    lcs = []

    while i > 0 and j > 0:
        if P[i - 1] == Q[j - 1]:
            lcs.append(P[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The LCS is built in reverse order, so we need to reverse it
    lcs.reverse()
    return lcs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user input from form
    P = request.form['sequence1'].strip().split(',')
    Q = request.form['sequence2'].strip().split(',')
    
    # Call the LCS function
    lcs = longest_common_subsequence(P, Q)
    
    return render_template('index.html', lcs=lcs, sequence1=P, sequence2=Q)

if __name__ == '__main__':
    app.run(debug=True)
