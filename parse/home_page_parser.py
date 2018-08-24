import os
import re
import requests

from html.parser import HTMLParser

class HomePageParser(HTMLParser):
    def __init__(self, year=2017):
        super().__init__()
        self.team_urls = []
        self.year = year

    def parse(self, uri):
        '''
        The only interface with this class is here, through parse.
        This function will return a list of team urls.
        '''
        self.base_uri = uri
        self.team_urls = []
        super().reset() # just in case there is bad data left behind
        if os.path.exists(uri):
            with open(uri, "r") as f:
                for line in f.readlines():
                    self.feed(line)
        else:
            content = requests.get(uri).text
            for line in content.splitlines():
                self.feed(line)
        return self.team_urls

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs:
            href = attrs[0][1]
            if re.match('.*' + str(self.year) + '/team/[0-9]+.*', href):
                uri = self.base_uri + href
                self.team_urls.append(uri)
