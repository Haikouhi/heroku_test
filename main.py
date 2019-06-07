from flask import Flask

app = FLask(__name__)

@app.route("/")
def hello():
    return "Hello World"