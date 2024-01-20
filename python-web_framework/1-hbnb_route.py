""" import Flask module """
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display ():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb ():
    return "HBNB"

if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0")
