import numpy

def fprint(f):
    print(fmt(f))

def fmt(f):
    return "%.02f" % f

class Ranker(object):
    def __init__(self, teams):
        self.teams = teams

    def index_stat(self, stat):
        power_indexes = {t : 0.0 for t in self.teams}
        for team in power_indexes.keys():
            power_indexes[team] = getattr(team, stat)
        mean = numpy.mean(list(power_indexes.values()))
        for team in power_indexes.keys():
            power_indexes[team] -= mean
        return power_indexes

    def rank(self):
        ppg = self.index_stat('points_scored_per_game_opp')
        print(ppg)
