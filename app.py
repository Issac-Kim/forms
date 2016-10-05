from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def forms():
    return render_template("main.html")

@app.route("/authenticate/", methods = ['POST'])
def do_things():
    d = request.form
    return d
if __name__ == '__main__':
    app.debug = True
    app.run()
