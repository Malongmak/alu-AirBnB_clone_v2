#!/usr/bin/python3
<<<<<<< HEAD
""" Web application listening on 0.0.0.0, port 5000 """
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
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
=======
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
    return "HBNB"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
=======
    app.run(host="0.0.0.0")
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
