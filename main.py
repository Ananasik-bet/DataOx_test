from asyncio import DatagramTransport
from parser import parse_url
from date_base import save_info_in_db
from google_sheets import write_into_sheets

data = parse_url('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')

# for elem in data:
#     save_info_in_db(image_url=elem[0], date=elem[1], cost=elem[2])

write_into_sheets(
    credential_file = 'service-account.json',
    spreadsheets = 'DataOx test',
    list_sheets = 'Room Info',
    data = data
)
print(len(data))