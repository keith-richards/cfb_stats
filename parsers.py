import sys

from html.parser import HTMLParser
from team import Team

class SimpleParser(object):
    def __init__(self, name, team):
        self.name = name
        self.team = team

class StringParser(SimpleParser):
    def parse(self, data):
        setattr(self.team, self.name, str(data))

class IntParser(SimpleParser):
    def parse(self, data):
        setattr(self.team, self.name, int(data))

class FloatParser(SimpleParser):
    def parse(self, data):
        setattr(self.team, self.name, float(data))

class SplitParser(object):
    def __init__(self, names, indexes, team, _type):
        self.names = names
        self.indexes = indexes
        self.team = team
        self._type = _type

    def parse(self, data):
        d = data.split(' - ')
        for i, name in zip(self.indexes, self.names):
            setattr(self.team, name, self._type(d[i]))

class SplitIntParser(SplitParser):
    def __init__(self, names, indexes, team):
        super().__init__(names, indexes, team, int)

class SplitFloatParser(SplitParser):
    def __init__(self, names, indexes, team):
        super().__init__(names, indexes, team, float)


class TeamHomePageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.team = Team()
        self.skip = True
        self.stat_index = 0
        self.stat_parsers = [
            StringParser('name', self.team),
            None,
            None,
            FloatParser('points_per_game', self.team),
            FloatParser('points_per_game_opp', self.team),
            None,
            SplitIntParser(['games', 'points_scored'], [0, 1], self.team),
            SplitIntParser(['points_scored_opp'], [1], self.team),
        ]

    def handle_starttag(self, tag, attrs):
        pass#print(tag, attrs)

    def handle_endtag(self, tag):
        pass#print("Got end", tag)

    def handle_data(self, data):
        if data.isspace():
            return
        if data == 'Team Statistics':
            self.skip = False
            return
        if 'Copyright' in data:
            self.skip = True
        if self.skip:
            return
        if self.stat_index < len(self.stat_parsers):
            parser = self.stat_parsers[self.stat_index]
            if parser:
                parser.parse(data)
        self.stat_index += 1
