from flask import Flask, render_template, request, session, redirect, url_for
from utils import readCSV

app = Flask(__name__)
app.secret_key = '\xcd\xb8\xb7o\x32\xc2\xdb_+\xe2\xde\xd1}\xd223\x76k\x2c\rDz\x12\x62l\xde\x2f\xf0 Qdr'

@app.route("/")
def m():
    for user in session:
        return redirect(url_for('home'))
    return render_template("main.html")

@app.route("/home/")
def home():
    return render_template('home.html', user = session['user'])

@app.route("/logout/", methods=['POST'])
def logout():
    r = request.form
    if "logout" in r:
        session.pop('user')
    return redirect(url_for('m'))

@app.route("/authenticate/", methods = ['POST'])
def log():
    r = request.form
    username = r['user']
    password = r['pass']
    session['user'] = username
    if "login" in r:
        s = readCSV.login(username, password)
        if s == "login failed":
            return s
        else:
            return redirect(url_for("home"))
    elif "register" in r:
        return readCSV.register(username, password)
        
    

if __name__ == '__main__':
    app.debug = True
    app.run()
