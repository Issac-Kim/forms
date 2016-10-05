from flask import Flask, render_template, request
from utils import readCSV
app = Flask(__name__)

@app.route("/login/")
def forms():
    return render_template("main.html")

@app.route("/register/")
def reg():
    return render_template("register.html")

@app.route("/authenticate/", methods = ['POST'])
def log():
    d = request.form
    return readCSV.login(d['user'], d['pass'])

@app.route("/membership/", methods = ['POST'])
def reg():
    d = request.form
    return readCSV.register(d['user'], d['pass'])

if __name__ == '__main__':
    app.debug = True
    app.run()
