from html.parser import HTMLParser

from cfb_stats.parse.parsers import *
from cfb_stats.common.team import Team

class TeamHomePageParser(HTMLParser):
    def __init__(self):
        super().__init__()

    def parse(self, filename):
        '''
        The only interface with this class is here, through parse.
        This function will return a team object, containing the parsed data.
        '''
        team = self.__initialize_team()
        self.skip = True
        self.stat_index = 0
        with open(filename, "r") as f:
            for line in f.readlines():
                self.feed(line)
        return team

    def __initialize_team(self):
        team = Team()
        self.stat_parsers = [
            StringParser('name', team),
            None,
            None,
            FloatParser('points_per_game', team),
            FloatParser('points_per_game_opp', team),
            None,
            SplitIntParser(['games', 'points_scored'], team),
            SplitIntParser(['points_scored_opp'], team, [1]),
            None,
            IntParser('first_downs', team),
            IntParser('first_downs_opp', team),
            None,
            SplitIntParser(['rushing_first_downs', 'passing_first_downs',
                            'penalty_first_downs'], team),
            SplitIntParser(['rushing_first_downs_opp', 'passing_first_downs_opp',
                            'penalty_first_downs_opp'], team),
            None,
            FloatParser('rushing_yards_per_attempt', team),
            FloatParser('rushing_yards_per_attempt_opp', team),
            None,
            SplitIntParser(['rushing_attempts', 'rushing_yards', 'rushing_tds'], team),
            SplitIntParser(['rushing_attempts_opp', 'rushing_yards_opp', 'rushing_tds_opp'], team),
            None,
            FloatParser('passing_rating', team),
            FloatParser('passing_rating_opp', team),
            None,
            IntParser('passing_yards', team),
            IntParser('passing_yards_opp', team),
            None,
            SplitIntParser(['passing_attempts', 'passing_completions',
                            'passing_interceptions', 'passing_tds'], team),
            SplitIntParser(['passing_attempts_opp', 'passing_completions_opp',
                            'passing_interceptions_opp', 'passing_tds_opp'], team),
            None,
            FloatParser('total_offense_yards_per_play', team),
            FloatParser('total_offense_yards_per_play_opp', team),
            None,
            SplitIntParser(['total_offense_plays', 'total_offense_yards'], team),
            SplitIntParser(['total_offense_plays_opp', 'total_offense_yards_opp'], team),
            None,
            FloatParser('punt_return_yards_per_return', team),
            FloatParser('punt_return_yards_per_return_opp', team),
            None,
            SplitIntParser(['punt_return_returns', 'punt_return_yards', 'punt_return_tds'], team),
            SplitIntParser(['punt_return_returns_opp', 'punt_return_yards_opp', 'punt_return_tds_opp'],
                           team),
            None,
            FloatParser('kickoff_return_yards_per_return', team),
            FloatParser('kickoff_return_yards_per_return_opp', team),
            None,
            SplitIntParser(['kickoff_return_returns', 'kickoff_return_yards', 'kickoff_return_tds'],
                           team),
            SplitIntParser(['kickoff_return_returns_opp', 'kickoff_return_yards_opp', 'kickoff_return_tds_opp'],
                           team),
            None,
            FloatParser('punting_yards_per_punt', team),
            FloatParser('punting_yards_per_punt_opp', team),
            None,
            SplitIntParser(['punting_punts', 'punting_yards'], team),
            SplitIntParser(['punting_punts_opp', 'punting_yards_opp'], team),
            None,
            SplitIntParser(['interception_returns', 'interception_yards', 'interception_tds'], team),
            SplitIntParser(['interception_returns_opp', 'interception_yards_opp', 'interception_tds_opp'], team),
            None,
            SplitIntParser(['fumbles', 'fumbles_lost'], team),
            SplitIntParser(['fumbles_opp', 'fumbles_lost_opp'], team),
            None,
            SplitIntParser(['penalties', 'penalties_yards'], team),
            SplitIntParser(['penalties_opp', 'penalties_yards_opp'], team),
            None,
            StringParser('time_of_possession', team),
            StringParser('time_of_possession_opp', team),
            None,
            PercentParser('third_down_conversion_percent', team),
            PercentParser('third_down_conversion_percent_opp', team),
            None,
            SplitIntParser(['third_down_conversion_attempts', 'third_down_conversions'], team),
            SplitIntParser(['third_down_conversion_attempts_opp', 'third_down_conversions_opp'], team),
            None,
            PercentParser('fourth_down_conversion_percent', team),
            PercentParser('fourth_down_conversion_percent_opp', team),
            None,
            SplitIntParser(['fourth_down_conversion_attempts', 'fourth_down_conversions'], team),
            SplitIntParser(['fourth_down_conversion_attempts_opp', 'fourth_down_conversions_opp'], team),
            None,
            PercentParser('red_zone_success_percent', team),
            PercentParser('red_zone_success_percent_opp', team),
            None,
            SplitIntParser(['red_zone_attempts', 'red_zone_scores'], team),
            SplitIntParser(['red_zone_attempts_opp', 'red_zone_scores_opp'], team),
            None,
            PercentParser('field_goal_success_percent', team),
            PercentParser('field_goal_success_percent_opp', team),
            None,
            SplitIntParser(['field_goal_attempts', 'field_goals'], team),
            SplitIntParser(['field_goal_attempts_opp', 'field_goals_opp'], team),
            None,
            PercentParser('pat_kicking_success_percent', team),
            PercentParser('pat_kicking_success_percent_opp', team),
            None,
            SplitIntParser(['pat_kicking_attempts', 'pat_kicking_made'], team),
            SplitIntParser(['pat_kicking_attempts_opp', 'pat_kicking_made_opp'], team),
            None,
            PercentParser('two_point_conversion_success_percent', team),
            PercentParser('two_point_conversion_success_percent_opp', team),
            None,
            SplitIntParser(['two_point_conversion_attempts', 'two_point_conversions_made'], team),
            SplitIntParser(['two_point_conversion_attempts_opp', 'two_point_conversions_made_opp'], team),
        ]
        return team

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
