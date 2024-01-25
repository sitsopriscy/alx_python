# Copy the previous task to a new script that starts a Flask web application:
# Your web application must be listening on 0.0.0.0, port 5000
# Routes:
# /: display “Hello HBNB!”
# /hbnb: display “HBNB”
# /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
# /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
# The default value of text is “is cool”
# You must use the option strict_slashes=False in your route definition


"""importing flask"""
from flask import Flask

"""creates the variable application name"""
app = Flask(__name__)

"""route to retrieve hello HBNB"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_text(text="is cool"):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
