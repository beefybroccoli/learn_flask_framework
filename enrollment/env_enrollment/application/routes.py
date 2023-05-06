from application import app, db
from flask import render_template, request, Response, json



courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}];

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    # return "<h1>Hello world - home page with more ...<h1>"
    return render_template("index.html", home=True)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html", contact=True)

@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="2019"):   
    return render_template("courses.html", courseData=courseData,courses=True, term=term)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/enrollment", methods=["POST"])
def enrollment():
    id = request.form['courseID']
    title = request.form['title']
    term = request.form['term']
    return render_template("enrollment.html", data={"id":id, "title":title, "term":term})

@app.route("/api/courses")
@app.route("/api/courses/<idx>")
def api(idx=None):
    if(idx == None):
        jsonData = courseData
    else:
        jsonData = courseData[int(idx)]
    return Response(json.dumps(jsonData),  mimetype="application/json")

class User(db.Document):
    user_id = db.IntField( unique=True)
    first_name = db.StringField( max_length = 50)
    last_name = db.StringField( max_length = 50)
    email = db.StringField( max_length = 50)
    password = db.StringField( max_length = 50)

@app.route("/user")
def user():
    User(user_id=1, first_name="Chris", last_name="James", email="christ_james@yahoo.com",password="123").save()
    User(user_id=2, first_name="John", last_name="James", email="John_james@yahoo.com",password="123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)