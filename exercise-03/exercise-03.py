from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = {}
organizations = ["Organization A", "Organization B", "Organization C", "Organization D", "Organization E"]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        if name and organization in organizations:
            users[name] = organization
            return redirect('/registered')
        else:
            error = "Please enter a valid name and organization"
            return render_template('index.html', organizations=organizations, error=error)
    return render_template('index.html', organizations=organizations)

@app.route('/registered')
def registered():
    return render_template('registered.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)