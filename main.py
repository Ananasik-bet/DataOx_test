from parser import parse_url
from date_base import create_room

data = parse_url('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')

for elem in data:
    create_room(image_url=elem[0], date=elem[1], cost=elem[2])

