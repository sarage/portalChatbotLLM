import requests
from bs4 import BeautifulSoup


def fetch_info_tunduk():
    url = "bhttps://portal.tunduk.kg/site/show_all"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="service-description")
    return content.text.strip() if content else None
