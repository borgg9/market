from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            result = number * 10
        except ValueError:
            result = "Please enter a valid number."
    return render_template_string('''
        <!doctype html>
        <html>
            <head>
                <title>Multiply by 10</title>
            </head>
            <body>
                <h1>Enter a number to multiply by 10</h1>
                <form method="post">
                    <input type="text" name="number">
                    <input type="submit" value="Multiply">
                </form>
                {% if result is not none %}
                    <h2>Result: {{ result }}</h2>
                {% endif %}
            </body>
        </html>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
