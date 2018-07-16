import bs4
import requests
from console import session

class CraigsList:
    def __init__(self):
        self.text = requests.get('https://newyork.craigslist.org/search/brk/aap').text
        self.soup = bs4.BeautifulSoup(self.text)

    def apartment_rows(self):
        # <li>
        return self.soup.find_all(class_="result-row")

    def create_craigslist_apts(self):
        apt_rows = []
        for apt_row in self.apartment_rows():
            cla = CraigsListApartment(apt_row)
            apt_rows.append(cla)
            apt = Apartment(price=cla.price(), title=cla.title())
            session.add(apt)
        session.commit()
        return apt_rows

class CraigsListApartment:
    def __init__(self, result_row):
        self.apt_soup = result_row

    def price(self):
        price_string = self.apt_soup.find(class_='result-price').text
        return int(price_string[1:])

    def title(self):
        return self.apt_soup.find(class_="result-title hdrlnk").text
