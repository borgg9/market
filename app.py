from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = request.form['number']
        result = int(number) * 10
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
