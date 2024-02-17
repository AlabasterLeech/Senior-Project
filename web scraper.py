"""
Module docstring
"""
#Imports
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#module level constants
_TEST_URL = "https://www.fussball.de/homepage#!/"

def main():
    #Full page scrape test code
    testscraper = webscraper()
    testscraper.seturl(_TEST_URL)
    testscraper.parse()
    testscraper.navigate()
    #print(testscraper.soup.prettify())

class webscraper():
    """
    The webscraper object serves as the overarching container for the complete functionality of the webscraper as described
    in the project proposal. A webscraper object can be initialized with a URL or passed one to scrape. Full functionality
    with ability to focus on only releveant data to come.
    """

    def __init__(self):
        self.url = None
        self.soup = None

    def seturl(self, url):
        self.url = url

    def geturl(self):
        return self.url

    def parse(self):
        try:
            page_request = requests.get(self.url)
            self.soup = BeautifulSoup(page_request.content, "html.parser")
        except:
            print("Parse Error")

    def navigate(self):
        try: 
            emulator = webdriver.Chrome()
            emulator.get(_TEST_URL)

            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[1]'))).click()
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[1]/ul/li[3]/a'))).click()
            #form = emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form')
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[2]'))).click()
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[2]/ul/li[2]/a'))).click()
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[3]'))).click()
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[3]/ul/li[2]/a'))).click()
            time.sleep(3)
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[4]'))).click()
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[4]/ul/li[2]/a'))).click()
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[5]'))).click()
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[5]/ul/li[2]/a'))).click()
            #WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[6]'))).click()
            #WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[6]/ul/li[2]/a'))).click()
            #WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]'))).click()
            #WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]/ul/li[2]/a'))).click()
            time.sleep(3)
            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[3]/button'))).click()
            print(emulator.current_url)
        except:
            print("Navigate Error")
if __name__ == '__main__':
    main()