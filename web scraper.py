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
#hard coded for testing data retrieval
_LEAGUE_URL = "https://www.fussball.de/spieltagsuebersicht/bfv-verbandsliga-baden-verbandsliga-herren-saison2324-baden/-/staffel/02M5JMALNO00000EVS5489B3VVRQ15EP-G#!/"
_TEAM_URL = "https://www.fussball.de/mannschaft/fv-fortuna-heddesheim-fv-fortuna-heddesheim-baden/-/saison/2324/team-id/011MIDDAF0000000VTVG0001VTR8C1K7#!/"
def main():
    #Full page scrape test code
    testscraper = webscraper()
    testscraper.seturl(_TEST_URL)
    testscraper.parse()
    #print(testscraper.soup.prettify())
    testscraper.seturl(_LEAGUE_URL)
    testscraper.parse()
    testscraper.grableaguedata()
    #testscraper.grabteamdata()
    testscraper.navigate()
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
            #league_list = emulator.find_elements(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[5]')
            emulator.get(_TEST_URL)
            more_li = True
            league_index = 10
            default_form_values = []
            reached_before = False
            for i in range(4):
                print('//*[@id="home-list"]/div/div[2]/div[7]/div/div/div/form/div[1]/div[1]/div['+str(i+1)+']')
                default_form_values.append(emulator.find_element(By.XPATH, '//*[@id="home-list"]/div/div[2]/div[7]/div/div/div/form/div[1]/div[1]/div['+str(i+1)+']').click())
            while more_li:
                try:
                    if(emulator.find_element(By.XPATH, '//*[@id="home-list"]/div/div[2]/div[7]/div/div/div/form/div[1]/div[1]/div[1]').text == default_form_values[0]):
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="home-list"]/div/div[2]/div[7]/div/div/div/form/div[1]/div[1]/div[1]'))).click()
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="home-list"]/div/div[2]/div[7]/div/div/div/form/div[1]/div[1]/ul/li[4]/a'))).click()
                    if(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[2]').text == default_form_values[1]):
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[2]'))).click()
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[2]/ul/li[3]'))).click()
                    if(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[3]').text == default_form_values[2]):
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[3]'))).click()
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[3]/ul/li[2]/a'))).click()
                        time.sleep(3)
                    if(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[4]').text == default_form_values[3]):
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[4]'))).click()
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[4]/ul/li[7]/a'))).click()
                        default_form_values.append(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[5]').text)
                    if(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[5]').text == default_form_values[4]):
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[5]'))).click()
                        league_xpath = '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[5]/ul/li[' + str(league_index) + ']/a'
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, league_xpath))).click()
                        default_form_values.append(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[6]').text)                    
                    if(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[6]').text != default_form_values[5]):
                        default_form_values.append(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]').text)
                        if(emulator.find_element(By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]').text != default_form_values[6]):
                            time.sleep(3)
                            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[3]/button'))).click()
                            print(emulator.current_url)
                        else:
                            print("Checkpoint 7")
                            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]'))).click()
                            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]/ul/li[2]/a'))).click()
                            time.sleep(3)
                            WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[3]/button'))).click()
                            print(emulator.current_url)
                    else:
                        print("Checkpoint 6")
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[6]'))).click()
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[6]/ul/li[2]/a'))).click()
                        time.sleep(3)
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]'))).click()
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[1]/div[7]/ul/li[2]/a'))).click()
                        time.sleep(3)
                        WebDriverWait(emulator, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="news-sidebar"]/div[1]/div/div/div/form/div[3]/button'))).click()
                        print(emulator.current_url)
                    emulator.get(_TEST_URL)
                except: 
                    if(league_index > 2):
                        print("Termintated without all league levels reached: li = " + league_index)
                    else:
                        print("Terminated at highest league level")
                    more_li = False
                league_index -= 1
        except:
            print("Navigate Error")

    def grableaguedata(self):
        try: 
            response = requests.get(_LEAGUE_URL)
            league_soup = BeautifulSoup(response.content, 'html.parser')
            #grab teams in league
            teams_list = []
            links_to_teams = []
            table = league_soup.find('div', id="fixture-league-tables")
            table_body = table.find('tbody')
                #alter to (find all tr where team names are listed) rather than searching for particular table's id
            rows = table_body.find_all('tr')

            for row in rows:
                col = row.find('td', {"class": "column-club"})
                teams_list.append(col.text.strip())
                col = row.find('a')
                links_to_teams.append(col.get('href'))
        except: 
            print("Error grabbing league data")

    def grabteamdata(self):
        try:
            response = requests.get(_TEAM_URL)
            league_soup = BeautifulSoup(response.content, 'html.parser')
            #grab players on team
            players_list = []
            links_to_players = []
            #table = league_soup.find('div', id="team-squad-table")
            #table_body = table.find('tbody')
            table_body = league_soup.find(By.XPATH, '//*[@id="team-squad-wrapper"]/div[2]/div[1]/div[2]/div[2]/table/tbody')
            print(table_body)
            #league_soup.dfsfortag(table)
            print(table_body.find(By.XPATH, '//*[@id="team-squad-wrapper"]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]'))
            #rows = table_body.find_all('tr')
            """
            for row in rows:
                col = row.find('td', {"class": "column-player"})
                players_list.append(col.text.strip())
                col = row.find('a')
                links_to_players.append(col.get('href'))
            """
        except:
            print("Error grabbing team data")

    def dfsfortag(self, tag):
        league_soup = self
        try: 
            table = tag
            table_body = table.find('tbody')
        except: 
            table_body = table.find('div')
            league_soup.dfsfortag(table_body)
if __name__ == '__main__':
    main()