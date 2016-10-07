from flask import Flask, render_template, request
from utils import readCSV
app = Flask(__name__)

@app.route("/")
def m():
    return render_template("main.html")

@app.route("/authenticate/", methods = ['POST'])
def log():
    r = request.form
    username = r['user']
    password = r['pass']
    if "login" in r:
        return login(username, password)
    elif "register" in r:
        return register(username, password)
    

if __name__ == '__main__':
    app.debug = True
    app.run()
