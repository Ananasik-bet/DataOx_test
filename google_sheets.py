import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

def write_into_sheets(spreadsheet_id, CREDENTIALS_FILE, data):

    values = ["Image URL", "Post Date", "Price"]
    for elem in data:
        for index in range(3):
            values.append(str(elem[index]))

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.built('sheets', 'v4', http=httpAuth)

    service.spreadsheets().values().batchUpdate(
        spreadsheetsId = spreadsheet_id,
        body = { 
            "valueInputOption": "USER_ENTERED",
            "data": [
                {
                    "range": f"A1:C{len(data) + 2}",
                    "majorDimension": "ROWS",
                    "values": values
                }
            ]
        }
    ).execute()