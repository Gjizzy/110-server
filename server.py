from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello World, Ch59!</p>"


@app.route("/cohort59")
def hi():
    return "<h1>Hello Cohort#59</h1>"


@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to the home page!"


@app.get("/api/students")
def students():
    print("Students endpoint accessed")
    student_names = [
        "Britney",
        "Tatiana",
        "Alexander",
        "James",
        "Ray",
        "Britney",
        "David",
        "Maryna",
        "Yaquelin",
    ]
    return student_names


# Path Parameter
@app.get("/greet/<string:name>")
def greet(name):
    return f"Hello {name}"


@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user = {"name": "peter", "age": 35}  # dictionary
    return user


app.run(debug=True)py server.py