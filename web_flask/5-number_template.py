#!/usr/bin/python3
<<<<<<< HEAD
""" Web application listening on 0.0.0.0, port 5000 """
from flask import Flask, render_template
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
"""
from flask import Flask
from flask import render_template
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/")
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Display HBNB! """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Display 'C' followed by the value of text
    Replace underscore _ symbols with a space
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    Display 'Python' followed by the value of text
    Replace underscore _ symbols with a space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """
    Display 'n is a number' only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
=======
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
