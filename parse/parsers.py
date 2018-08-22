class SimpleParser(object):
    def __init__(self, name, team):
        self.name = name
        self.team = team

class StringParser(SimpleParser):
    def parse(self, data):
        data = data.strip()
        setattr(self.team, self.name, str(data))

class IntParser(SimpleParser):
    def parse(self, data):
        data = data.strip()
        if data == '-':
            setattr(self.team, self.name, 0)
        else:
            setattr(self.team, self.name, int(data))

class FloatParser(SimpleParser):
    def parse(self, data):
        data = data.strip()
        if data == '-':
            setattr(self.team, self.name, 0.0)
        else:
            setattr(self.team, self.name, float(data))

class PercentParser(SimpleParser):
    def parse(self, data):
        data = data.strip()
        if data == '-':
            setattr(self.team, self.name, 0.0)
        else:
            setattr(self.team, self.name, float(data.strip('%')))

class SplitParser(object):
    def __init__(self, names, team, _type, indexes):
        self.names = names
        self.team = team
        self._type = _type
        self.indexes = indexes
        if not self.indexes:
            self.indexes = list(range(len(self.names)))
        assert(isinstance(self.names, list))
        assert(isinstance(self.indexes, list))

    def parse(self, data):
        data = data.split(' - ')
        for i, name in zip(self.indexes, self.names):
            val = data[i].strip()
            if val == '-':
                setattr(self.team, self.name, self._type(0.0))
            else:
                setattr(self.team, name, self._type(val))

class SplitIntParser(SplitParser):
    def __init__(self, names, team, indexes=None):
        super().__init__(names, team, int, indexes)

class SplitFloatParser(SplitParser):
    def __init__(self, names, team, indexes=None):
        super().__init__(names, team, float, indexes)
