from flask import Flask, request, render_template_string

app = Flask(__name__)

def compare_chefs(chef1, chef2):
    chef1_points, chef2_points = 0, 0

    for i in range(3):
        if chef1[i] > chef2[i]:
            chef1_points += 1
        elif chef1[i] < chef2[i]:
            chef2_points += 1

    return chef1_points, chef2_points

@app.route('/', methods=['GET', 'POST'])
def index():
    chef1_points, chef2_points = 0, 0
    if request.method == 'POST':
        try:
            chef1 = [int(request.form[f'chef1_{i}']) for i in range(1, 4)]
            chef2 = [int(request.form[f'chef2_{i}']) for i in range(1, 4)]
            chef1_points, chef2_points = compare_chefs(chef1, chef2)
        except ValueError:
            return "Invalid input. Please enter valid numbers."

    # Read the HTML file and render it with points
    with open('p1.html', 'r') as file:
        html_content = file.read()
    
    return render_template_string(html_content, chef1_points=chef1_points, chef2_points=chef2_points)

if __name__ == "__main__":
    app.run(debug=True)
