import requests
from bs4 import BeautifulSoup


def get(link: str) -> dict:

    response = requests.get(link)

    soup = BeautifulSoup(response.content, 'html.parser')

    text_list = [elem.text for elem in soup.find_all(class_ = 'd-link deco-link')]

    return {'album': text_list[0], 'artist': text_list[1], 'title': text_list[3]}
