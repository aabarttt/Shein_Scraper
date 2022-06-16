from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from duo.single import get_data

offers = []
url = input("URL : ")
quantity = int(input("HOW MANY OFFERS ? : "))

s = Service("C:/Users/barto/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.maximize_window()


def allow_cookies():
    try:
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/i').click()
        # sleep(2)
        # driver.find_element(By.XPATH, '/html/body/div[9]/div[1]').click()
        sleep(0.5)
    except:
        allow = input('PLEASE ALLOW COOKIES : ')


allow_cookies()
kafelki = driver.find_elements(By.CLASS_NAME, 'S-product-item__wrapper')

for i in range(quantity):
    a = kafelki[i].find_element(By.TAG_NAME, 'a')
    href = a.get_attribute('href')
    print(href)
    offer = get_data(href, i)
    print(offer)
    offers.append(offer)

print()
print(offers)
