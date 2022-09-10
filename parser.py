import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def parse_url(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    data = soup.find('div', id="MainContainer").find('div', id="mainPageContent")\
        .find('div', class_="col-2").find('main').find_all('div')[1].find_all('div', class_="search-item")


    parse_data = []
    for elem in data:
        image_url = elem.find('img').get('data-src')

        date_parse = elem.find('div', class_='location').find('span', class_="date-posted").text
        if 'ago' in date_parse:
            date_now = datetime.now()
            if int(date_parse.split(' ')[1]) > date_now.hour:
                yesterday = date_now - timedelta(days=1)
                date = f"{yesterday.day}-{yesterday.month}-{yesterday.year}"
            else:
                date = f"{date_now.day}-{date_now.month}-{date_now.year}"
        else:
            date_parse = date_parse.split('/')
            date = f"{date_parse[0]}-{date_parse[1]}-{date_parse[2]}"

        cost = elem.find('div', class_="price").text.replace(' ', '').replace('\n', '')

        parse_data.append([image_url, date, cost])

    return parse_data

