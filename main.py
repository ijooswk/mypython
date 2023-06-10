import requests
from bs4 import BeautifulSoup
import json

def web_scraper(url):
    """this function is to get the json file parsed from the response of the url
    For example:
    url = 'https://www.abc.com'
    url can be any website, it will return the json file parsed from the response of the url
    """ 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find whatever you want.
    results = soup.find(id="footer")
    return results

web_scraper('https://www.google.com')