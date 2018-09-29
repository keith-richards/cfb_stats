#! /usr/bin/env python3
import os
import sys
import argparse
import multiprocessing

from cfb_stats.rank.ranker import Ranker
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

def main():
    argparser = argparse.ArgumentParser(description='Rank teams from data from cfbstats.com')
    argparser.add_argument('--procs', help='Multiprocess the parsers.', default=4, type=int)
    argparser.add_argument('--source_dir', required=True, help='Path to the directory of html containing all team html.')
    args = argparser.parse_args(sys.argv[1:])

    teams = parse_teams(args)
    ranker = Ranker(teams)
    ranker.rank()

if __name__ == '__main__':
    main()
