from flask import Flask, render_template, jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/acerca")
@app.route("/acerca/<nombre>")
def about(nombre=None):
    return render_template('about.html', nombre=nombre)

@app.route("/suma/<int:a>/<int:b>")
def suma(a,b):
    c = a+b
    return str(c)

@app.route("/suma/<int:a>/<int:b>/json")
def sumajson(a,b):
    return jsonify(a=a,b=b,suma=a+b)

@app.route("/divide/<int:a>/<int:b>")
def divide(a,b):
    c = 0
    if b != 0:
        c = a/b
        return str(c)
    else:
        return "tried to divide by 0"
    

@app.route("/divide/<int:a>/<int:b>/json")
def dividejson(a,b):
    if b != 0:
        c = a/b
        
        return jsonify(a=a,b=b,division=c)
    else:
        return jsonify("division by 0")
    
