import requests
from bs4 import BeautifulSoup
import json
from webobject import WebObject

def web_scraper(url):
    """this function is to get the json file parsed from the response of the url
    The webobject will be created from the webobject class
    """ 
    wo = WebObject(url)
    
    # find whatever you want.
    results = wo.search_for_id("footer")
    print(results)
    return results

web_scraper('https://www.google.com')