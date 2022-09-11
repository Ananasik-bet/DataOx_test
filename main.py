from parser import get_count, parse_url
from date_base import save_info_in_db
from google_sheets import write_into_sheets

urls = get_count('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-1000/c37l1700273')
count = len(urls)
url1 = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-'
url2 = '/c37l1700273'
data = []

for page in range(count):
    url = url1 + str(page + 1) + url2
    data.append(parse_url(url))


for page in data:
    for elem in page:
        save_info_in_db(image_url=elem[0], date=elem[1], cost=elem[2])


write_into_sheets(
    credential_file = 'service-account.json',
    spreadsheets = 'DataOx test',
    list_sheets = 'Room Info',
    data = data
)
