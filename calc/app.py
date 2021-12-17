# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def adding():
    """Returb a + b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route("/sub")
def subtracting():
    """Return a - b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def multiplying():
    """Return a * b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route("/div")
def dividing():
    """Return a / b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)

@app.route("/math/<op>")
def maths(op):
    """Provide a math operation and an a and b parameter, returns result"""
    ops = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
    }
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = ops[op](a,b)
    return str(result)