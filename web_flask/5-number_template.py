#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """
    returns a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    returns a string
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    display C  followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    display Python , followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """
    display n is a number only if n is an integer
    """
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def only_if_number(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
