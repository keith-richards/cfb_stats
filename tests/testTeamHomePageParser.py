
import sys

import unittest
from unittest.mock import MagicMock

sys.path.append("../")
from parsers import TeamHomePageParser
from parsers import SplitIntParser

class TestSplitIntParser(unittest.TestCase):
    def test_split_int(self):
        data = '0 - 12 - 273'
        o = MagicMock()
        p = SplitIntParser(['k', 'e'], [1,2], o)
        p.parse(data)
        self.assertEqual(o.k, 12)
        self.assertEqual(o.e, 273)

class TestTeamHomePageParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = TeamHomePageParser()
        with open("team_home_page.html", "r") as f:
            for line in f.readlines():
                cls.parser.feed(line)
        cls.team = cls.parser.team

    def test_name(self):
        self.assertEqual(self.team.name, "Hawai'i")
    def test_points_per_game(self):
        self.assertEqual(self.team.points_per_game, 22.8)
    def test_games(self):
        self.assertEqual(self.team.games, 12)
    def test_points_scored(self):
        self.assertEqual(self.team.points_scored, 273)
    # def test_first_downs(self):
    #     self.assertEqual(self.team.first_downs, 238)
    # def test_rushing_first_downs(self):
    #     self.assertEqual(self.team.rushing_first_downs, 101)
    # def test_passing_first_downs(self):
    #     self.assertEqual(self.team.passing_first_downs, 120)
    # def test_penalty_first_downs(self):
    #     self.assertEqual(self.team.penalty_first_downs, 17)
    # def test_rushing_yards_per_attempt(self):
    #     self.assertEqual(self.team.rushing_yards_per_attempt, 4.80)
    # def test_rushing_attempts(self):
    #     self.assertEqual(self.team.rushing_attempts, 420)
    # def test_rushing_yards(self):
    #     self.assertEqual(self.team.rushing_yards, 2018)
    # def test_rushing_tds(self):
    #     self.assertEqual(self.team.rushing_tds, 15)
    # def test_passing_rating(self):
    #     self.assertEqual(self.team.passing_rating, 128.39)
    # def test_passing_yards(self):
    #     self.assertEqual(self.team.passing_yards, 2814)
    # def test_passing_attempts(self):
    #     self.assertEqual(self.team.passing_attempts, 423)
    # def test_passing_completions(self):
    #     self.assertEqual(self.team.passing_completions, 260)
    # def test_passing_interceptions(self):
    #     self.assertEqual(self.team.passing_interceptions, 8)
    # def test_passing_tds(self):
    #     self.assertEqual(self.team.passing_tds, 19)
    # def test_total_offense_yards_per_play(self):
    #     self.assertEqual(self.team.total_offense_yards_per_play, 5.73)
    # def test_total_offense_plays(self):
    #     self.assertEqual(self.team.total_offense_plays, 843)
    # def test_total_offense_yards(self):
    #     self.assertEqual(self.team.total_offense_yards, 4832)
    # def test_punt_return_yards_per_return(self):
    #     self.assertEqual(self.team.punt_return_yards_per_return, 5.00)
    # def test_punt_return_yards(self):
    #     self.assertEqual(self.team.punt_return_yards, 30)
    # def test_punt_return_returns(self):
    #     self.assertEqual(self.team.punt_return_returns, 6)
    # def test_punt_return_tds(self):
    #     self.assertEqual(self.team.punt_return_tds, 0)
    # def test_kickoff_return_yards_per_return(self):
    #     self.assertEqual(self.team.kickoff_return_yards_per_return, 19.80)
    # def test_kickoff_return_yards(self):
    #     self.assertEqual(self.team.kickoff_return_yards, 812)
    # def test_kickoff_return_returns(self):
    #     self.assertEqual(self.team.kickoff_return_returns, 41)
    # def test_kickoff_return_tds(self):
    #     self.assertEqual(self.team.kickoff_return_tds, 0)
    # def test_punting_yards_per_punt(self):
    #     self.assertEqual(self.team.punting_yards_per_punt, 42.07)
    # def test_punting_punts(self):
    #     self.assertEqual(self.team.punting_punts, 41)
    # def test_punting_yards(self):
    #     self.assertEqual(self.team.punting_yards, 812)
    # def test_interception_returns(self):
    #     self.assertEqual(self.team.interception_returns, 9)
    # def test_interception_yards(self):
    #     self.assertEqual(self.team.interception_yards, 130)
    # def test_interception_tds(self):
    #     self.assertEqual(self.team.interception_tds, 1)
    # def test_fumbles(self):
    #     self.assertEqual(self.team.fumbles, 16)
    # def test_fumbles_lost(self):
    #     self.assertEqual(self.team.fumbles_lost, 6)
    # def test_penalties(self):
    #     self.assertEqual(self.team.penalties, 93)
    # def test_penalties_yards(self):
    #     self.assertEqual(self.team.penalties_yards, 826)
    # def test_time_of_possession(self):
    #     self.assertEqual(self.team.time_of_possession, "31:28.17")
    # def test_third_down_conversion_attempts(self):
    #     self.assertEqual(self.team.third_down_conversion_attempts, 167)
    # def test_third_down_conversions(self):
    #     self.assertEqual(self.team.third_down_conversions, 64)
    # def test_fourth_down_conversion_attempts(self):
    #     self.assertEqual(self.team.fourth_down_conversion_attempts, 28)
    # def test_fourth_down_conversions(self):
    #     self.assertEqual(self.team.fourth_down_conversions, 10)
    # def test_red_zone_attempts(self):
    #     self.assertEqual(self.team.red_zone_attempts, 43)
    # def test_red_zone_scores(self):
    #     self.assertEqual(self.team.red_zone_scores, 30)
    # def test_field_goal_attempts(self):
    #     self.assertEqual(self.team.field_goal_attempts, 9)
    # def test_field_goals(self):
    #     self.assertEqual(self.team.field_goals, 4)
    # def test_pat_kicking_attempts(self):
    #     self.assertEqual(self.team.pat_kicking_attempts, 35)
    # def test_pat_kicking_made(self):
    #     self.assertEqual(self.team.pat_kicking_made, 33)
    # def test_two_point_conversion_attempts(self):
    #     self.assertEqual(self.team.two_point_conversion_attempts, 2)
    # def test_two_point_conversions_made(self):
    #     self.assertEqual(self.team.two_point_conversions_made, 1)

    # def test_points_per_game_opp(self):
    #     self.assertEqual(self.team.points_per_game_opp, 33.9)
    # def test_points_scored_opp(self):
    #     self.assertEqual(self.team.points_scored_opp, 407)
    # def test_first_downs_opp(self):
    #     self.assertEqual(self.team.first_downs_opp, 274)
    # def test_rushing_first_downs_opp(self):
    #     self.assertEqual(self.team.rushing_first_downs_opp, 124)
    # def test_passing_first_downs_opp(self):
    #     self.assertEqual(self.team.passing_first_downs_opp, 129)
    # def test_penalty_first_downs_opp(self):
    #     self.assertEqual(self.team.penalty_first_downs_opp, 21)
    # def test_rushing_yards_per_attempt_opp(self):
    #     self.assertEqual(self.team.rushing_yards_per_attempt_opp, 5.25)
    # def test_rushing_attempts_opp(self):
    #     self.assertEqual(self.team.rushing_attempts_opp, 480)
    # def test_rushing_yards_opp(self):
    #     self.assertEqual(self.team.rushing_yards_opp, 2522)
    # def test_rushing_tds_opp(self):
    #     self.assertEqual(self.team.rushing_tds_opp, 23)
    # def test_passing_rating_opp(self):
    #     self.assertEqual(self.team.passing_rating_opp, 162.05)
    # def test_passing_yards_opp(self):
    #     self.assertEqual(self.team.passing_yards_opp, 2983)
    # def test_passing_attempts_opp(self):
    #     self.assertEqual(self.team.passing_attempts_opp, 334)
    # def test_passing_completions_opp(self):
    #     self.assertEqual(self.team.passing_completions_opp, 213)
    # def test_passing_interceptions_opp(self):
    #     self.assertEqual(self.team.passing_interceptions_opp, 9)
    # def test_passing_tds_opp(self):
    #     self.assertEqual(self.team.passing_tds_opp, 29)
    # def test_total_offense_yards_per_play_opp(self):
    #     self.assertEqual(self.team.total_offense_yards_per_play_opp, 6.76)
    # def test_total_offense_plays_opp(self):
    #     self.assertEqual(self.team.total_offense_plays_opp, 814)
    # def test_total_offense_yards_opp(self):
    #     self.assertEqual(self.team.total_offense_yards_opp, 5505)
    # def test_punt_return_yards_per_return_opp(self):
    #     self.assertEqual(self.team.punt_return_yards_per_return_opp, 7.44)
    # def test_punt_return_yards_opp(self):
    #     self.assertEqual(self.team.punt_return_yards_opp, 201)
    # def test_punt_return_returns_opp(self):
    #     self.assertEqual(self.team.punt_return_returns_opp, 27)
    # def test_punt_return_tds_opp(self):
    #     self.assertEqual(self.team.punt_return_tds_opp, 0)
    # def test_kickoff_return_yards_per_return_opp(self):
    #     self.assertEqual(self.team.kickoff_return_yards_per_return_opp, 20.36)
    # def test_kickoff_return_yards_opp(self):
    #     self.assertEqual(self.team.kickoff_return_yards_opp, 957)
    # def test_kickoff_return_returns_opp(self):
    #     self.assertEqual(self.team.kickoff_return_returns_opp, 47)
    # def test_kickoff_return_tds_opp(self):
    #     self.assertEqual(self.team.kickoff_return_tds_opp, 2)
    # def test_punting_yards_per_punt_opp(self):
    #     self.assertEqual(self.team.punting_yards_per_punt_opp, 40.36)
    # def test_punting_punts_opp(self):
    #     self.assertEqual(self.team.punting_punts_opp, 44)
    # def test_punting_yards_opp(self):
    #     self.assertEqual(self.team.punting_yards_opp, 1776)
    # def test_interception_returns_opp(self):
    #     self.assertEqual(self.team.interception_returns_opp, 8)
    # def test_interception_yards_opp(self):
    #     self.assertEqual(self.team.interception_yards_opp, 79)
    # def test_interception_tds_opp(self):
    #     self.assertEqual(self.team.interception_tds_opp, 1)
    # def test_fumbles_opp(self):
    #     self.assertEqual(self.team.fumbles_opp, 18)
    # def test_fumbles_lost_opp(self):
    #     self.assertEqual(self.team.fumbles_lost_opp, 6)
    # def test_penalties_opp(self):
    #     self.assertEqual(self.team.penalties_opp, 68)
    # def test_penalties_yards_opp(self):
    #     self.assertEqual(self.team.penalties_yards_opp, 619)
    # def test_time_of_possession_opp(self):
    #     self.assertEqual(self.team.time_of_possession_opp, "28:31.83")
    # def test_third_down_conversion_attempts_opp(self):
    #     self.assertEqual(self.team.third_down_conversion_attempts_opp, 164)
    # def test_third_down_conversions_opp(self):
    #     self.assertEqual(self.team.third_down_conversions_opp, 80)
    # def test_fourth_down_conversion_attempts_opp(self):
    #     self.assertEqual(self.team.fourth_down_conversion_attempts_opp, 18)
    # def test_fourth_down_conversions_opp(self):
    #     self.assertEqual(self.team.fourth_down_conversions_opp, 12)
    # def test_red_zone_attempts_opp(self):
    #     self.assertEqual(self.team.red_zone_attempts_opp, 50)
    # def test_red_zone_scores_opp(self):
    #     self.assertEqual(self.team.red_zone_scores_opp, 40)
    # def test_field_goal_attempts_opp(self):
    #     self.assertEqual(self.team.field_goal_attempts_opp, 18)
    # def test_field_goals_opp(self):
    #     self.assertEqual(self.team.field_goals_opp, 8)
    # def test_pat_kicking_attempts_opp(self):
    #     self.assertEqual(self.team.pat_kicking_attempts_opp, 54)
    # def test_pat_kicking_made_opp(self):
    #     self.assertEqual(self.team.pat_kicking_made_opp, 51)
    # def test_two_point_conversion_attempts_opp(self):
    #     self.assertEqual(self.team.two_point_conversion_attempts_opp, 1)
    # def test_two_point_conversions_made_opp(self):
    #     self.assertEqual(self.team.two_point_conversions_made_opp, 0)
