from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES= ['https://www.googleapis.com/auth/spreadsheets']

creds= None
creds= service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
sheetID= '1-BUCK6upv_LehdOwkKuaK461VF54Cq2RP-lvPZIl4gQ'

service= build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet= service.spreadsheets()
result= sheet.values().get(spreadsheetId=sheetID,
                             range="Sheet1!A2:B500").execute()
values= result.get('values', [])

eqpt= "milk" #equipment name
qty= "21" #equipment quantity

data= [[eqpt, qty], ["koala", "2"]] #array of arrays, could make data equals textfield input for frontend
res= service.spreadsheets().values().append(spreadsheetId=sheetID, range="Sheet1!A1:B1", valueInputOption="USER_ENTERED", 
                                                        insertDataOption="INSERT_ROWS", body={"values":data}).execute()
print(res)
#print(result)