import sys
import argparse
import multiprocessing

from cfb_stats.parse.home_page_parser import HomePageParser
from cfb_stats.parse.team_home_page_parser import TeamHomePageParser

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def parse_team_home_pages(uris, q):
    parser = TeamHomePageParser()
    for u in uris:
        q.put(parser.parse(u))

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Parse stats from cfbstats.com')
    argparser.add_argument('--procs', help='Multiprocess the parsers', default=1, type=int)
    args = argparser.parse_args(sys.argv[1:])

    parser = HomePageParser()
    team_urls = parser.parse('http://www.cfbstats.com')

    processes = []
    doneq = multiprocessing.Queue()
    chunk_size = int(len(team_urls) / args.procs)
    for chunk in chunks(team_urls, chunk_size):
        p = multiprocessing.Process(target=parse_team_home_pages, args=(chunk, doneq))
        processes.append(p)
        p.start()

    teams = []
    for _ in team_urls:
        teams.append(doneq.get())

    for p in processes:
        p.join()

    print('done done')
