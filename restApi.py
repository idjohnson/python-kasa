from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/on")
def turn_on():
    return "Turn On!"

@app.route("/off")
def turn_off():
    return "Turn Off!"

@app.route("/swap")
def turn_swap():
    return "Swap on and off!"