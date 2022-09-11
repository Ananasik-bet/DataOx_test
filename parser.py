import requests
from bs4 import BeautifulSoup
import dateparser

def get_count(url):

    # Find pages count
    result = requests.get(url)
    soup_result = BeautifulSoup(result.text, 'html.parser')
    count = int(soup_result.find('head').find('title').text.split(' ')[-1])

    # Generate URL for all pages
    urls = [f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page_index}/c37l1700273'\
        for page_index in range(count)]

    return urls


def parse_url(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    data = soup.find('div', id="MainContainer").find('div', id="mainPageContent")\
        .find('div', class_="col-2").find('main').find_all('div')[1].find_all('div', class_="search-item")


    parse_data = []
    for elem in data:
        image_url = elem.find('img').get('data-src')

        date_parse = elem.find('div', class_='location').find('span', class_="date-posted").text
        if '/' in date_parse:
            date_parse = date_parse.split('/')
            date = f'{date_parse[0]}-{date_parse[1]}-{date_parse[2]}'
        else:
            date = dateparser.parse(date_parse).strftime("%d-%m-%Y")

        cost = elem.find('div', class_="price").text.replace(' ', '').replace('\n', '')

        parse_data.append([image_url, date, cost])

    return parse_data

