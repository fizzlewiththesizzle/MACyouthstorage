from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html", content="Testing")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/signout")
def signout():   
    return render_template("signout.html")

if __name__ == "__main__":
    app.run(debug=True)
