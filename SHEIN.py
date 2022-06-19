from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from passwords import user_password, user_login
from time import sleep


class SheinDownloader:
    def __init__(self, url: str):
        path = ".../chromedriver.exe"
        s = Service(path)
        self.url = url
        self.driver = webdriver.Chrome(service=s)

    def click_element(self, element):
        for i in range(3):
            sleep(2**i)
            try:
                self.driver.find_element(By.XPATH, element).click()
                print(f"try nr {i+1} success")
            except:
                print(f"try nr {i+1} failed")

    def allow_cookies(self):
        try:
            self.click_element('//*[@id="onetrust-accept-btn-handler"]')
            self.click_element('/html/body/div[1]/div[3]/div[1]/div/i')
            sleep(0.5)
        except Exception as e:
            allow = input('Please Allow cookies, when you finish click enter :')

    def open_webside(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.allow_cookies()

    def get_offers_url(self):
        item_wrapers = self.driver.find_elements(By.CLASS_NAME, 'S-product-item__wrapper')
        urls = []
        for item in item_wrapers:
            a = item.find_element(By.TAG_NAME, 'a')
            href = a.get_attribute('href')
            urls.append(href)

        return urls

    def get_name(self):
        try:
            name = self.driver.find_element(By.CLASS_NAME, 'product-intro__head-name').text
            return name
        except Exception as e:
            print(f'parse name | en error ocured : {e}')
            return ""

    def get_price(self):
        try:
            price_div = self.driver.find_element(By.CLASS_NAME, 'from')
            price = price_div.find_element(By.TAG_NAME, 'span').text
            return price
        except Exception as e:
            print(f'parse price | en error ocured : {e}')
            return ""

    def get_color(self):
        try:
            color = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/span/span').text
            return color
        except Exception as e:
            print(f'parse color | en error ocured : {e}')
            return ""

    def get_photo_src(self, photo):
        photo.click()
        big_photo = self.driver.find_element(By.XPATH, '/html/body/div[15]/div/div/div/div/div[2]/div/img')
        src = big_photo.get_attribute('src')
        return src

    def get_images(self):
        try:
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/img').click()
            sleep(1)
            photos_ul = self.driver.find_element(By.XPATH, '/html/body/div[15]/div/div/div/div/div[1]/ul')
            photos = photos_ul.find_elements(By.TAG_NAME, 'li')

            srcs = [self.get_photo_src(photo) for photo in photos]

            self.driver.find_element(By.XPATH, '/html/body/div[15]/div/i').click()
            return srcs

        except Exception as e:
            print(f'parse images | en error ocured : {e}')
            return ""

    def get_description(self):
        try:
            try:
                self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/h2').click()
            except:
                self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/h2/i').click()
            sleep(1)

            description = []
            full_dict = self.driver.find_elements(By.CLASS_NAME, 'product-intro__description-table-item')
            for line in full_dict:
                key = line.find_element(By.CLASS_NAME, 'key').text
                value = line.find_element(By.CLASS_NAME, 'val').text
                description.append(key + '  ' + value + '  |  ')

        except Exception as e:
            print(f'parse description | en error ocured : {e}')
            return ""

    def get_offer_data(self, offer_url):
        self.driver.get(offer_url)
        sleep(5)

        offer = {
        'name': self.get_name(),
        'price': self.get_price(),
        'url': offer_url,
        'size': ['XS', 'S', 'M', 'L', 'XL'],
        'color': self.get_color(),
        'imgs': self.get_images(),
        'description': self.get_description()
        }

        return offer

    def get_many_offers(self, quantity):
        offers_url = self.get_offers_url()
        if quantity > len(offers_url):
            print(f"Able to return only {len(offers_url)} from {quantity} requested")
        else:
            offers_url = offers_url[0:quantity]

        offers = [self.get_offer_data(url) for url in offers_url]

        return offers

