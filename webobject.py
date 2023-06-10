#This is the class for the web object from the url to keep the response and the parsed json file

import requests
from bs4 import BeautifulSoup
import json

class WebObject:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def search_for_id(self, id):
        return self.soup.find(id=id)

    def get_url(self):
        return self.url
    
    def get_response(self):
        return self.response
    
    def get_soup(self):
        return self.soup
    
    def get_json(self, content):
        return json.loads(content.text)
    
    def get_json_pretty(self, content):
        return json.dumps(json.loads(content.text), indent=4, sort_keys=True)
    
    def get_json_pretty_print(self, content):
        print(json.dumps(json.loads(content.text), indent=4, sort_keys=True))
    