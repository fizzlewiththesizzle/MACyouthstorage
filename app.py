from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html", content="Testing")

@app.route("/add", methods= ["GET", "POST"])
def add():

    if request.method == "POST":

        req= request.form

        equipmentName= req["equipmentName"]
        equipmentQuantity= req["equipmentQuantity"]

        print(equipmentName, equipmentQuantity)

        return redirect(request.url)

    return render_template("add.html")

@app.route("/signout", methods= ["GET", "POST"])
def signout(): 

    if request.method == "POST": 

        req= request.form

        userName= req["userName"]
        equipmentName= req["equipmentName"]
        equipmentQuantity= req["equipmentQuantity"]

        print(userName, equipmentName, equipmentQuantity)

        return redirect(request.url)
      
    return render_template("signout.html")

if __name__ == "__main__":
    app.run(debug=True)