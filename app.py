from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__, static_folder="assets")

todos=[(True,'Get Milk'),(False,'Learn Flask'), (False,'Go to Office'), (False,'Learn AWS'), (False,'Sleep')]

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("home.html",todos=todos)

@app.route("/<string:todo>")
def todo_item(todo:str):
    for completed,item in todos:
        if todo==item:
            completed_todo="[x]" if completed else "[]"
            title=f"{completed_todo} - {item}"
            return render_template("todo.html",todo=item, completed=completed, title=title)
        else:
            continue
    return render_template("not-found.html",todo=item, title="Not Found")

@app.route("/fizzbuzz")
def fizzbuzz():
    return render_template("FizzBuzz.html")

def square(value):
    return (value**0.5).is_integer()

app.jinja_env.tests['square']=square
   