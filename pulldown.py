#! /usr/bin/env python3
import os
import re
import sys
import argparse
import requests
from html.parser import HTMLParser

session = requests.Session()

class PullDownBase(HTMLParser):
    def __init__(self, url, args):
        super().__init__()
        self.url = url
        self.args = args
        self.content = None

    def _write(self, filename):
        if self.args.local:
            return
        path = os.path.abspath(os.path.join(str(self.args.year), str(self.args.week)))
        if not os.path.exists(path):
            os.makedirs(path)
        filename = os.path.join(path, filename)
        with open(filename, 'w') as f:
            f.write(self.content)

    def pull(self):
        if self.args.local:
            with open(self.args.local, 'r') as f:
                self.content = f.read()
        else:
            self.content = session.get(self.url).text
        for line in self.content.splitlines():
            self.feed(line)

class TeamHomePagePullDown(PullDownBase):
    def __init__(self, url, args):
        super().__init__(url, args)

    def pull(self):
        super().pull()
        team_id = self.url.split("/index.html")[0].split("/")[-1]
        self._write(team_id + ".html")

class HomePagePullDown(PullDownBase):
    def __init__(self, url, args):
        super().__init__(url, args)
        self.team_home_urls = []

    def pull(self):
        super().pull()
        for t in self.team_home_urls:
            puller = TeamHomePagePullDown(t, self.args)
            puller.pull()

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs:
            href = attrs[0][1]
            if re.match('.*' + str(self.args.year) + '/team/[0-9]+.*', href):
                url = self.url + href
                self.team_home_urls.append(url)

def main():
    arg_parser = argparse.ArgumentParser(description='Pull down all the html for the current week')
    arg_parser.add_argument('--year', type=int, help='The year will also specify the folder to put the data in', required=True)
    arg_parser.add_argument('--week', type=int, help='The week will be a subfolder', required=True)
    arg_parser.add_argument('--local', type=str, help='dev only; home page filename', default=None)
    arg_parser.add_argument('--url', type=str, help='http://www.cfbstats.com', default='http://www.cfbstats.com')
    args = arg_parser.parse_args(sys.argv[1:])

    puller = HomePagePullDown(args.url, args)
    puller.pull()

if __name__ == '__main__':
    main()
