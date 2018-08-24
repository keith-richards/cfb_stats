import unittest
from cfb_stats.parse.home_page_parser import HomePageParser


class TestHomePageParser(unittest.TestCase):
    def test_num_teams(self):
        parser = HomePageParser()
        teams = parser.parse("home.html")
        self.assertEqual(len(teams), 130)
