from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def check_number():
    try:
        number = int(request.form['number'])
        if number % 2 == 0:
            result = 'Even'
        else:
            result = 'Odd'
    except ValueError:
        result = 'Not an integer'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)