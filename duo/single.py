def get_data(link, nr):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from passwords import user_password, user_login
    import webbrowser
    from time import sleep


    #zmienne
    PATH = "C:/Users/barto/Downloads/chromedriver/chromedriver.exe"

    name, current_url, url = '', '', ''
    price, ide = 0, 0
    sizes, srcs, related_links, description, offers = [], [], [], [], []

    url = link
    quantity = 1
    s = Service(PATH)
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
            allow = input('Do it your own :')

    allow_cookies()

    for i in range(quantity):
        # # 001
        try:
            name = driver.find_element(By.CLASS_NAME, 'product-intro__head-name').text
            print('001 : ✅')
        except:
            print('001 : ✖')

        # # 002
        try:
            price_div = driver.find_element(By.CLASS_NAME, 'from')
            price = price_div.find_element(By.TAG_NAME, 'span').text
            print('002 : ✅')
        except:
            print('002 : ✖')

        # 003
        try:
            current_url = driver.current_url
            print('003 : ✅')
        except:
            print('003 : ✖')

        # 004
        try:
            ide = nr
            print('004 : ✅')
        except:
            print('004 : ✖')

        # 005
        try:
            sizes = ['XS', 'S', 'M', 'L', 'XL']
            print('005 : ✅')
        except:
            print('005 : ✖')

        # 006
        try:
            color = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/span/span').text
            print('006 : ✅')
        except:
            color = 'LOOK AT THE PHOTOS'
            print('006 : ✖')

        # 007
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/img').click()
            sleep(1)
            print('7.1')
            photos_ul = driver.find_element(By.XPATH, '/html/body/div[15]/div/div/div/div/div[1]/ul')
            print('7.2')
            photos = photos_ul.find_elements(By.TAG_NAME, 'li')
            print('7.3')
            srcs = []
            for photo in photos:
                photo.click()
                big_photo = driver.find_element(By.XPATH, '/html/body/div[15]/div/div/div/div/div[2]/div/img')
                src = big_photo.get_attribute('src')
                srcs.append(src)
            print('7.4')
            driver.find_element(By.XPATH, '/html/body/div[15]/div/i').click()
            print('007 : ✅')
        except Exception as e:
            print(f'007 : ✖  {e}')

        # 008 related
        try:
            related = driver.find_elements(By.CLASS_NAME, 'product-intro__color-block')
            current_relate = driver.find_elements(By.CLASS_NAME, 'product-intro__color-block_active')
            print('8.1')

            if len(related) == 0:
                related = driver.find_elements(By.CLASS_NAME, 'product-intro__color-radio')
                current_relate = driver.find_elements(By.CLASS_NAME, 'product-intro__color-radio_active')
            related_links = []
            print('8.2')

            for relate in related:
                if relate != current_relate[0]:
                    relate.click()
                    link = driver.current_url
                    related_links.append(link)
                    sleep(0.5)
                # else:
                    #print('the same')
            print('8.3')
            current_relate[0].click()
            print('008 : ✅')
        except:
            print('008 : ✖')

        # print(related_links)

        # 009 opis
        try:
            try:
                driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/h2').click()
                print('9.1')
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/h2/i').click()
                print('9.2')

            sleep(1)
            description = []
            full_dict = driver.find_elements(By.CLASS_NAME, 'product-intro__description-table-item')
            print('9.3')
            for line in full_dict:
                key = line.find_element(By.CLASS_NAME, 'key').text
                value = line.find_element(By.CLASS_NAME, 'val').text
                description.append(key + '  ' + value + '  |  ')
            print('009 : ✅')
        except:
            print('009 : ✖')

        # 010 model

        offer = {
            'name': name,
            'price': price,
            'url': current_url,
            'id': ide,
            'size': sizes,
            'color': color,
            'imgs': srcs,
            'related': related_links,
            'description': description
        }

        print('OFFER ' + str(nr+1) + ' : ' + str(offer))
        print()
    driver.close()
    return offer


