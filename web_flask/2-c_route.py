#!/usr/bin/python3
<<<<<<< HEAD
""" Web application listening on 0.0.0.0, port 5000 """
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
=======
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
