from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
options = Options()
options.add_argument('--headless')
driver=webdriver.Chrome(options=options)
def get_html(link):
    driver.get(link)
    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    return soup
def close_driver():
    driver.close()
    driver.quit()