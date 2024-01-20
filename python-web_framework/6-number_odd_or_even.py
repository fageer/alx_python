""" import Flask module """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display ():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb ():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c (text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python (text):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def display_n (n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_nInt (n):
    return render_template("5-number.html", number = n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_nOddOrEven (n):
    return render_template("6-number_odd_or_even.html", number = n)


if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0")
