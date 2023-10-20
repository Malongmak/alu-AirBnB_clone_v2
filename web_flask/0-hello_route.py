#!/usr/bin/python3
<<<<<<< HEAD
""" Web application listening on 0.0.0.0, port 5000 """
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/")
def hello_hbnb():
    """ Display Hello HBNB! """
=======
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
=======
    app.run(host="0.0.0.0")
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
