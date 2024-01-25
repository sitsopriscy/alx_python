"""# Copy the previous task to a new script that starts a Flask web application:
# Your web application must be listening on 0.0.0.0, port 5000
# Routes:
# /: display “Hello HBNB!”
# /hbnb: display “HBNB”
# You must use the option strict_slashes=False in your route definition"""


"""to import flask"""
from flask import Flask

"""to create the variable application name"""
app = Flask(__name__)

"""a route to display display Hello HBNB! """


@app.route("/", strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


"""a route to display display HBNB! """


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# """importing flask"""
# from flask import Flask

# """creates the variable application name"""
# app = Flask(__name__)

# """route for retrieving hello HBNB"""


# @app.route("/", strict_slashes=False)
# def hello_hbnb():
#     return "Hello HBNB!"


# @app.route("/hbnb", strict_slashes=False)
# def hbnb():
#     return "HBNB"


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
