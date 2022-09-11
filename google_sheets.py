import gspread

def write_into_sheets(credential_file, spreadsheets, list_sheets, data):

    service_account = gspread.service_account(credential_file)
    sheets = service_account.open(spreadsheets)

    worksheet = sheets.worksheet(list_sheets)

    info_sheet = []
    for page in data:
        for elem in page:
            info_sheet.append(elem)
    worksheet.update(
        f"A1:C{len(info_sheet) + 2}", info_sheet
    )
