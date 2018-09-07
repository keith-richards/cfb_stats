from scipy.stats import poisson

def fprint(f):
    print(fmt(f))

def fmt(f):
    return "%.02f" % f

class PoissonDistribution(object):
    def __init__(self, team):
        self.team = team
        self.distribution = {}

    def _poisson_dist(self, _lambda, _k):
        # fast but overflows
        # return 100.0 * math.exp(-1 * _lambda) * ((_lambda ** _k) / factorial(_k))
        return 100.0 * poisson.pmf(_k, _lambda)

    def compute_distribution(self, stat):
        self.distribution[stat] = []
        total_chance = 0
        for i in range(1000):
            team_stat = self.team.get_per_game_stat(stat)
            chance = self._poisson_dist(team_stat, i)
            self.distribution[stat].append(chance)
            total_chance += chance
            if total_chance > 99.99:
                return

    def get_chance_stat(self, stat, _k):
        d = self.distribution[stat]
        return d[_k]

    def get_chance_gt_stat(self, stat, _k):
        d = self.distribution[stat]
        return sum(d[_k:])

    def get_chance_lt_stat(self, stat, _k):
        d = self.distribution[stat]
        return sum(d[0:_k])

    def print_stat(self, stat):
        for i in self.distribution[stat]:
            fprint(i)

class Ranker(object):
    def __init__(self, teams):
        self.teams = teams
        self.dists = {}

    def rank(self):
        for team in self.teams:
            if team.games == 0:
                continue
            self.dists[team.name] = pd = PoissonDistribution(team)
            pd.compute_distribution('points_per_game')
            #pd.compute_distribution('total_offense_yards')

        pd = self.dists['Utah']
        fprint(pd.get_chance_gt_stat('points_per_game', 34))
