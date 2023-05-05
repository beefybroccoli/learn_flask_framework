from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    # return "<h1>Hello world - home page with more ...<h1>"
    return render_template("index.html", login=True)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")
