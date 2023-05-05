from application import app
from flask import render_template

@app.route("/")
@app.route("/home")
@app.route("/contact")

def home():
    # return "<h1>Hello world - home page with more ...<h1>"
    return render_template("index.html")

def contact():
    return "<h1>Hello world - contact page<h1>"
