"""
Module docstring
"""
#Imports
from bs4 import BeautifulSoup
import requests

#module level constants
_TEST_URL = "https://www.fussball.de/homepage#!/"

def main():
    #Full page scrape test code
    testscraper = webscraper()
    testscraper.seturl(_TEST_URL)
    testscraper.parse()
    print(testscraper.soup.prettify())
    

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

    
if __name__ == '__main__':
    main()

