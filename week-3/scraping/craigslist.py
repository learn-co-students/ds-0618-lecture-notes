import bs4
import requests

class CraigsList:
    def __init__(self):
        self.text = requests.get('https://newyork.craigslist.org/search/brk/aap').text
        self.soup = bs4.BeautifulSoup(self.text)

    def apartment_rows(self):
        return self.soup.find_all(class_="result-row")

    def apartment(self):
        return self.apartment_rows()[0]

    def price(self):
        price_string = self.apartment().find(class_='result-price').text
        return int(price_string[1:])
