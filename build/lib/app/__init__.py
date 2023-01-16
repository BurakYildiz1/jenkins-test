from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Jenkins"
    
@app.route("/hello")
def hello_world():
    return "Hello, World!"