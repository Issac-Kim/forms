from flask import Flask, render_template, request

app = Flask(__name__)
user = "issac"
password = "kim"

@app.route("/")
def forms():
    return render_template("main.html")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    d = request.form
    if d['pass'] == password:
        if d['user'] == user:
            return "login successful"
        else:
            return "problem with login"
    else:
        return "problem with login"
if __name__ == '__main__':
    app.debug = True
    app.run()
