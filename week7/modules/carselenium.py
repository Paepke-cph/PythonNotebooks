import bs4
from car import car
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BilBasen():
    def __init__(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.get('https://www.bilbasen.dk/')
        self.browser.implicitly_wait(3)

    def clicker(self, click_this):
        try:
            click_this.click()
        except:
            try:
                accept_btn_cookies = self.browser.find_element_by_id(
                    "onetrust-accept-btn-handler")
                accept_btn_cookies.click()
                sleep(1)
                click_this.click()
            except:
                print('Could not click the cookie button')
        sleep(1)

    def no_leasing_search(self, search_car):
        leasing_label_checkbox = self.browser.find_element_by_css_selector(
            "[data-track-action=\"leasing-toggle\"]")
        self.clicker(leasing_label_checkbox)

        search_bar_element = self.browser.find_element_by_css_selector(
            "[placeholder=\"Søg på bil\"]")
        search_bar_element.send_keys(search_car)

        search_btn_element = self.browser.find_element_by_css_selector(
            ".btn.bb-btn-secondary.header-free-search-button")
        self.clicker(search_btn_element)
        return self.browser.current_url

    def get_all_cars_info(self, search_url):
        self.browser.get(search_url)
        soup = bs4.BeautifulSoup(self.browser.page_source, "html.parser")
        select_colXS6 = soup.select(
            "#srp-content .row.listing.bb-listing-clickable > .col-xs-6")
        filtered_colXS6 = filter(lambda x: len(
            x.select('.row')[0].find_all('div')) == 5, select_colXS6)
        car_links = soup.find_all('a', {'class': 'listing-heading darkLink'})
        cars = []
        for url, info_element in zip(car_links, filtered_colXS6):
            tmp_url = "https://www.bilbasen.dk" + url.get("href")
            html_divs = info_element.select('.row')[0].find_all('div')
            tmp_km = html_divs[2].text
            tmp_price = html_divs[4].text.split(" ")[0]
            cars.append(car(tmp_url, tmp_price, tmp_km))
        return cars

    def done(self):
        self.browser.quit()


if __name__ == "__main__":
    test = BilBasen()
    try:
        url_bentley = test.no_leasing_search("Mercedes")
        cars = test.get_all_cars_info(url_bentley)
        cheapest_car_pr_km = car.cheapest_pr_km(cars)
        print(cheapest_car_pr_km)
    finally:
        test.done()