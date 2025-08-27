from flask import Flask, request 

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello World, Ch59!</p>"

# http://127.0.0.1:500/home
@app.route("/cohort59")
def hi():
    return "<h1>Hello Cohort#59</h1>"


@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to the home page!"

# http://127.0.0.1
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
# http://127.0.0.1:5000/greet/<string:name
@app.get("/greet/<string:name>")
def greet(name):
    return f"Hello {name}"


@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user = {"name": "peter", "age": 35}  # dictionary
    return user


# http://127.0.0.0:500/about
@app.get("/about")
def about_me():
    return "<h1> About me page </h1>"


products = ["Laptop", "Mouse", "Keyboard"]

# http:..127.0.0.11:5000/api/product
@app.get("/api/product")
def get_products():
    return products


# http://127.0.0.0:5000/api/product/count
@app.get("/api/product/count")
def get_product_count():
    return {"count": len(products)}


students = [
    {"id": 1, "name": "Bruce", "age": 54, "email": "batman@gmail.com"},
    {"id": 2, "name": "Pam", "age": 29, "email": "pam@gmail.com"},
]

@app.get("/students")
def get_students():
    return students


@app.post("/students")
def add_student():
    data = request.json
    students.append(data)
    return {"new_student":data}

app.run(debug=True)
#app.run(debug=True, port=5555)

@app.get("/students")
def get_students():
    return students




app.run(debug=True)
# app.run(debug=True, port=5555)