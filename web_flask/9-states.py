#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

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


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """
    /number_odd_or_even/<n>: display a HTML page only if n is an integer
    """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def list_all_states():
    """
    init all state
    """
    state_list = storage.all('State')
    return render_template('7-states_list.html', state_list=state_list)


@app.route('/cities_by_states', strict_slashes=False)
def list_all_states_and_cities():
    """
    init states and cities
    """
    list_state_and_cities = storage.all('State')
    return render_template('8-cities_by_states.html',
                           list_state_and_cities=list_state_and_cities)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html',
                           states=states, id=id)


@app.teardown_appcontext
def teardown_session(self):
    """
    teardown session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
