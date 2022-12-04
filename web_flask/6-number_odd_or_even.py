#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    var = text.replace('_', ' ')
    return "C " + var


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text="is cool"):
    var = text.replace('_', ' ')
    return "Python " + var


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template_route(n):
    return render_template("5-number.html", variable=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    var = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html",
                                variable=n, whatami=var)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
