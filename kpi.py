#! /usr/bin/env python3
import os
import sys
import argparse
import multiprocessing

import numpy

from cfb_stats.parse.team_home_page_parser import TeamHomePageParser

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def parse_team_home_pages(filenames, q):
    parser = TeamHomePageParser()
    for f in filenames:
        q.put(parser.parse(f))

def parse_teams(args):
    team_html_filenames = [os.path.abspath(os.path.join(args.source_dir, p)) for p in os.listdir(args.source_dir)]

    processes = []
    doneq = multiprocessing.Queue()
    chunk_size = int(len(team_html_filenames) / args.procs)
    for chunk in chunks(team_html_filenames, chunk_size):
        p = multiprocessing.Process(target=parse_team_home_pages, args=(chunk, doneq))
        processes.append(p)
        p.start()

    teams = []
    for _ in team_html_filenames:
        teams.append(doneq.get())

    for p in processes:
        p.join()

    return teams

class Indexes(object):
    def __init__(self, teams):
        self.teams = teams
        self.points_per_game_index = self._index_stat('points_scored_per_game')
        self.points_per_game_opp_index = self._index_stat('points_scored_per_game_opp', invert=True)
        # compute the following min and max to use as the current year's scoring curve bounds
        self.min_points_per_game = min(list(self.points_per_game_index.values()))
        self.max_points_per_game = max(list(self.points_per_game_index.values()))
        self.min_points_per_game_opp = min(list(self.points_per_game_opp_index.values()))
        self.max_points_per_game_opp = max(list(self.points_per_game_opp_index.values()))

    def _index_stat(self, stat, invert=False):
        power_indexes = {}
        for team in self.teams:
            power_indexes[team.name] = getattr(team, stat)
        l = list(power_indexes.values())
        mean = numpy.mean(l)
        for team in self.teams:
            power_indexes[team.name] -= mean
            if invert:
                power_indexes[team.name] *= -1
        return power_indexes

    def __getitem__(self, team_name):
        return self.points_per_game_index[team_name], self.points_per_game_opp_index[team_name]

    def predict_matchup(self, team1_name, team2_name):
        team_1_by = 0
        team_2_by = 0
        t1o, t1d = self[team1_name]
        t2o, t2d = self[team2_name]

        team1_od_offset = t1o - t2d
        if team1_od_offset < 0:
            team_2_by = -team1_od_offset
        else:
            team_1_by = team1_od_offset
        team2_od_offset = t2o - t1d
        if team2_od_offset > 0:
            team_2_by += team2_od_offset
        else:
            team_1_by += -team2_od_offset

        point_spread = team_1_by - team_2_by
        if point_spread < 1 and point_spread > -1:
            return "Toss up", point_spread
        elif point_spread > 0:
            return team1_name, point_spread
        else:
            return team2_name, -point_spread


def main():
    argparser = argparse.ArgumentParser(description='Rank teams from data from cfbstats.com')
    argparser.add_argument('--procs', help='Multiprocess the parsers.', default=4, type=int)
    argparser.add_argument('--source_dir', required=True, help='Path to the directory of html containing all team html.')
    argparser.add_argument('--team', default=None)
    argparser.add_argument('--matchup', default=None)
    args = argparser.parse_args(sys.argv[1:])

    teams = parse_teams(args)
    indexes = Indexes(teams)

    if args.team:
        kpi = indexes[args.team.strip()]
        print("%s:\nOffensive index: %.02f\nDefensive index: %.02f" % (args.team, kpi[0], kpi[1]))
        return

    if args.matchup:
        team1 = args.matchup.split(',')[0].strip()
        team2 = args.matchup.split(',')[-1].strip()
        winner = indexes.predict_matchup(team1, team2)

        print("%s by %.02f" % (winner[0], winner[1]))



if __name__ == '__main__':
    main()
