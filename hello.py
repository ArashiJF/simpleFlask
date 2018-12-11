from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"

@app.route("/acerca")
@app.route("/acerca/<nombre>")
def about(nombre=None):
    return render_template('about.html', nombre=nombre)

@app.route("/suma/<float:a>/<float:b>")
@app.route("/suma/<float:a>/<int:b>")
@app.route("/suma/<int:a>/<float:b>")
@app.route("/suma/<int:a>/<int:b>")
@app.route("/suma/<int:a>/<int:b>/<string:json>")
@app.route("/suma/<float:a>/<float:b>/<string:json>")
@app.route("/suma/<float:a>/<int:b>/<string:json>")
@app.route("/suma/<int:a>/<float:b>/<string:json>")
def suma(a,b,json=None):
    if json == None:
        c = a+b
        return str(c)
    else:
        c = a+b
        return jsonify(a=a,b=b,suma=a+b)


@app.route("/divide/<float:a>/<float:b>")
@app.route("/divide/<int:a>/<int:b>")
@app.route("/divide/<float:a>/<int:b>")
@app.route("/divide/<int:a>/<float:b>")
@app.route("/divide/<int:a>/<int:b>/<string:json>")
@app.route("/divide/<float:a>/<float:b>/<string:json>")
@app.route("/divide/<float:a>/<int:b>/<string:json>")
@app.route("/divide/<int:a>/<float:b>/<string:json>")
def divide(a,b,json=None):
    if json == None:
        if b != 0:

            c = a/b
            return str(c)
        else:
            return "tried to divide by 0"
    else:
        if b != 0:
            c = a/b
            return jsonify(a=a,b=b,division=c)
        else:
            return jsonify(error="Division entre 0")
