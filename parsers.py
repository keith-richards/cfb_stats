import sys

from html.parser import HTMLParser
from team import Team

class TeamHomePageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.team = Team()
        self.start = False

    def handle_starttag(self, tag, attrs):
        pass#print(tag, attrs)
    
    def handle_endtag(self, tag):
        pass#print("Got end", tag)
    
    def handle_data(self, data):
        if data.isspace():
            return
        if data == 'Team Statistics':
            self.start = True
        if not self.start:
            return
        print("got data", data)


