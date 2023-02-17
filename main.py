import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)


def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub(' ', str(data))


def get_crawl(URL):
    driver.get(URL)
    html = driver.page_source
    soup7 = BeautifulSoup(html, 'html.parser')
    ex_id_divs = soup7.find('div', {'id': 'view_content'})
    crawl_data = remove_html_tags(ex_id_divs)
    return crawl_data


def close_popup():
    main = driver.window_handles

    for i in main:
        if i != main[0]:
            driver.switch_to.window(i)
            driver.close()


def send_message(text):
    url = 'http://localhost:8080'
    payload = {'text': text}
    requests.post(url, json=payload)


driver.implicitly_wait(3)
driver.get('https://sso.online.tableau.com/public/login')
login_x_path1 = '/html/body/div/div/form/div[8]/button/span[1]/span'
login_x_path2 = '/html/body/div/div/form/div[8]/button'
close_popup();
driver.find_element(by=By.NAME, value='email').send_keys('yskim@dnabro.com')
driver.find_element(by=By.XPATH, value=login_x_path1).click()
driver.find_element(by=By.NAME, value='password').send_keys('DnaBro1004*')
driver.find_element(by=By.XPATH, value=login_x_path2).click()

popup_path = '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div/div/button'
driver.find_element(by=By.XPATH, value=popup_path).click()

explore_path = '/html/body/div[1]/div/div[1]/div/div/div/div[1]/nav/ul/li[9]/div/a/img'
driver.find_element(by=By.XPATH, value=explore_path).click()

default_path = '/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[' \
               '1]/section/div[2]/div/div/div/div[1]/div/div/a '
driver.find_element(by=By.XPATH, value=default_path).click()

mainPage_path = '/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[' \
                '1]/section/div[1]/div/div/div/div[1]/div/div/a '
driver.find_element(by=By.XPATH, value=mainPage_path).click()

moon_test4_path = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[' \
                  '1]/section/div[9]/div/div/div/div[1]/div/div/a '
driver.find_element(by=By.XPATH, value=moon_test4_path).click()

elements = driver.find_elements(By.CSS_SELECTOR, '.CardView_action-row-name_fqcwmei')

for e in elements:
    print(e.text)

send_message(e.text)
while (True):
    pass
# try:
#     url = url_sample
#     data = get_crawl(url)
#     df = pd.DataFrame([{
#         'contents': data
#     }])
# finally:
#     print(df.copy().shape)
# /html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/section/div[2]/div/div/div/div[1]/div/div/a
