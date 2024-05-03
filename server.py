from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/sign-in")
def index():
    return render_template('sign-in.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True, port=5004)