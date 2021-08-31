from flask import Flask, redirect, url_for, render_template, request
from googleapiclient.discovery import build
from google.oauth2 import service_account

app = Flask(__name__)

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES= ['https://www.googleapis.com/auth/spreadsheets']

creds= None
creds= service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
sheetID= '1-BUCK6upv_LehdOwkKuaK461VF54Cq2RP-lvPZIl4gQ'

service= build('sheets', 'v4', credentials=creds)

@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html", content="Testing")

@app.route("/add", methods= ["GET", "POST"])
def add():

    if request.method == "POST":
        equipmentName = request.form.get("equipmentName")
        equipmentQuantity = request.form.get("equipmentQuantity")

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheetID, range="Sheet1!A2:B500").execute()
        values = result.get('values', [])

        data = [[equipmentName, equipmentQuantity]] #array of arrays, could make data equals textfield input for frontend
        res = service.spreadsheets().values().append(spreadsheetId=sheetID, range="Sheet1!A1:B1", valueInputOption="USER_ENTERED", 
                                                                insertDataOption="INSERT_ROWS", body={"values":data}).execute()
        print(res)

        return redirect(request.url)
    return render_template("add.html")

@app.route("/signout", methods= ["GET", "POST"])
def signout(): 

    if request.method == "POST": 

        userName = request.form.get("userName")
        equipmentName = request.form.get("equipmentName")
        equipmentQuantity= request.form.get("equipmentQuantity")

        print(userName, equipmentName, equipmentQuantity)

        return redirect(request.url)
      
    return render_template("signout.html")

if __name__ == "__main__":
    app.run(debug=True)

