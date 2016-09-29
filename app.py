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
    print request.form
    return "hi"
if __name__ == '__main__':
    app.debug = True
    app.run()
