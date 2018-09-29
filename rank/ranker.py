from collections import OrderedDict

def fprint(f):
    print(fmt(f))

def fmt(f):
    return "%.02f" % f

class Ranker(object):
    def __init__(self, teams):
        self.teams = teams
        self.ranks = {t.name : [ ] for t in teams}

    def _finalize_ranks(self):
        final_ranks = {t.name : 0.0 for t in self.teams}
        for name, ranks in self.ranks.items():
            final_ranks[name] = sum(ranks) / float(len(ranks))
        return OrderedDict(sorted(final_ranks.items(), key=lambda r: r[-1], reverse=True))

    def _rank_stat(self, stat, weight=1, low_stat=False):
        mean = sum([getattr(t, stat) for t in self.teams]) / float(len(self.teams))
        for t in self.teams:
            statistic = getattr(t, stat) - mean
            if low_stat:
                statistic *= -1
            for i in range(weight):
                self.ranks[t.name].append(statistic)

    def rank(self):
        self._rank_stat('points_scored_per_game', weight=2)
        # self._rank_stat('first_downs_per_game')
        # self._rank_stat('rushing_tds_per_game')
        # self._rank_stat('passing_tds_per_game')
        # self._rank_stat('total_offense_yards_per_play', weight=3)
        # self._rank_stat('total_offense_yards_per_game', weight=3)
        # self._rank_stat('passing_rating')

        self._rank_stat('points_scored_opp_per_game', low_stat=True, weight=2)
        # self._rank_stat('first_downs_opp_per_game', low_stat=True)
        # self._rank_stat('rushing_tds_opp_per_game', low_stat=True)
        # self._rank_stat('passing_tds_opp_per_game', low_stat=True)
        # self._rank_stat('total_offense_yards_per_play_opp', low_stat=True, weight=3)
        # self._rank_stat('total_offense_yards_per_game_opp', low_stat=True, weight=3)
        # self._rank_stat('passing_rating_opp', low_stat=True)

        final_ranks = self._finalize_ranks()

        count = 0
        for name, rank in final_ranks.items():
            print(name, rank)
            count += 1
            if count > 25:
                break
