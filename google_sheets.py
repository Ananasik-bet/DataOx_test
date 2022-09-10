import gspread


def write_into_sheets(credential_file, spreadsheets, list_sheets, data):

    data.insert(0, ["Image URL", "Post Date", "Price"])
    

    service_account = gspread.service_account(credential_file)
    sheets = service_account.open(spreadsheets)

    worksheet = sheets.worksheet(list_sheets)

    worksheet.update(
        f"A1:C{len(data) + 3}", data
    )
