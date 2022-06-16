from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from passwords import user_password, user_login
from time import sleep


PATH = "C:/Users/barto/Downloads/chromedriver/chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s)


driver.get("https://pl.shein.com/free-trial-center/'index")
driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[1]/a/i').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[4]/button[1]/span').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/p/a[2]').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[1]/div/div/input').send_keys( 'Bartosz1kwiecien@gmail.com')
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/div/input').send_keys( 'KapitalizacjaDlaPlebsu123')
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/button/span').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div/div/div[1]/button').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/div/div/div/div[5]/span').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[6]/div/ul/li[1]/span').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/a[1]').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div[2]/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/span[1]/div/div').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div[2]/div[6]/div[3]/div/div/div[2]/div/div[3]/button').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div[2]/div[7]/div[3]/div/div/div[2]/div/div[3]/button').click()
sleep(1)
