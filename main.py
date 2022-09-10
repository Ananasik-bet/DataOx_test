from parser import parse_url
from date_base import save_info_in_db
from google_sheets import write_into_sheets

data = parse_url('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')

for elem in data:
    save_info_in_db(image_url=elem[0], date=elem[1], cost=elem[2])

write_into_sheets(
    spreadsheet_id='1YIv5VFtd4Np3y0axMek7SSMyuPWaam5EjS10CfuJx8w',
    CREDENTIALS_FILE='creds.json',
    data=data
    )
