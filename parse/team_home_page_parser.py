from html.parser import HTMLParser
from cfb_stats.parse.parsers import *
from cfb_stats.common.team import Team

class TeamHomePageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.team = Team()
        self.skip = True
        self.stat_index = 0
        self.stat_parsers = [
            StringParser('name', self.team),
            None,
            None,
            FloatParser('points_per_game', self.team),
            FloatParser('points_per_game_opp', self.team),
            None,
            SplitIntParser(['games', 'points_scored'], self.team),
            SplitIntParser(['points_scored_opp'], self.team, [1]),
            None,
            IntParser('first_downs', self.team),
            IntParser('first_downs_opp', self.team),
            None,
            SplitIntParser(['rushing_first_downs', 'passing_first_downs',
                            'penalty_first_downs'], self.team),
            SplitIntParser(['rushing_first_downs_opp', 'passing_first_downs_opp',
                            'penalty_first_downs_opp'], self.team),
            None,
            FloatParser('rushing_yards_per_attempt', self.team),
            FloatParser('rushing_yards_per_attempt_opp', self.team),
            None,
            SplitIntParser(['rushing_attempts', 'rushing_yards', 'rushing_tds'], self.team),
            SplitIntParser(['rushing_attempts_opp', 'rushing_yards_opp', 'rushing_tds_opp'], self.team),
            None,
            FloatParser('passing_rating', self.team),
            FloatParser('passing_rating_opp', self.team),
            None,
            IntParser('passing_yards', self.team),
            IntParser('passing_yards_opp', self.team),
            None,
            SplitIntParser(['passing_attempts', 'passing_completions',
                            'passing_interceptions', 'passing_tds'], self.team),
            SplitIntParser(['passing_attempts_opp', 'passing_completions_opp',
                            'passing_interceptions_opp', 'passing_tds_opp'], self.team),
            None,
            FloatParser('total_offense_yards_per_play', self.team),
            FloatParser('total_offense_yards_per_play_opp', self.team),
            None,
            SplitIntParser(['total_offense_plays', 'total_offense_yards'], self.team),
            SplitIntParser(['total_offense_plays_opp', 'total_offense_yards_opp'], self.team),
            None,
            FloatParser('punt_return_yards_per_return', self.team),
            FloatParser('punt_return_yards_per_return_opp', self.team),
            None,
            SplitIntParser(['punt_return_returns', 'punt_return_yards', 'punt_return_tds'], self.team),
            SplitIntParser(['punt_return_returns_opp', 'punt_return_yards_opp', 'punt_return_tds_opp'],
                           self.team),
            None,
            FloatParser('kickoff_return_yards_per_return', self.team),
            FloatParser('kickoff_return_yards_per_return_opp', self.team),
            None,
            SplitIntParser(['kickoff_return_returns', 'kickoff_return_yards', 'kickoff_return_tds'],
                           self.team),
            SplitIntParser(['kickoff_return_returns_opp', 'kickoff_return_yards_opp', 'kickoff_return_tds_opp'],
                           self.team),
            None,
            FloatParser('punting_yards_per_punt', self.team),
            FloatParser('punting_yards_per_punt_opp', self.team),
            None,
            SplitIntParser(['punting_punts', 'punting_yards'], self.team),
            SplitIntParser(['punting_punts_opp', 'punting_yards_opp'], self.team),
            None,
            SplitIntParser(['interception_returns', 'interception_yards', 'interception_tds'], self.team),
            SplitIntParser(['interception_returns_opp', 'interception_yards_opp', 'interception_tds_opp'], self.team),
            None,
            SplitIntParser(['fumbles', 'fumbles_lost'], self.team),
            SplitIntParser(['fumbles_opp', 'fumbles_lost_opp'], self.team),
            None,
            SplitIntParser(['penalties', 'penalties_yards'], self.team),
            SplitIntParser(['penalties_opp', 'penalties_yards_opp'], self.team),
            None,
            StringParser('time_of_possession', self.team),
            StringParser('time_of_possession_opp', self.team),
            None,
            PercentParser('third_down_conversion_percent', self.team),
            PercentParser('third_down_conversion_percent_opp', self.team),
            None,
            SplitIntParser(['third_down_conversion_attempts', 'third_down_conversions'], self.team),
            SplitIntParser(['third_down_conversion_attempts_opp', 'third_down_conversions_opp'], self.team),
            None,
            PercentParser('fourth_down_conversion_percent', self.team),
            PercentParser('fourth_down_conversion_percent_opp', self.team),
            None,
            SplitIntParser(['fourth_down_conversion_attempts', 'fourth_down_conversions'], self.team),
            SplitIntParser(['fourth_down_conversion_attempts_opp', 'fourth_down_conversions_opp'], self.team),
            None,
            PercentParser('red_zone_success_percent', self.team),
            PercentParser('red_zone_success_percent_opp', self.team),
            None,
            SplitIntParser(['red_zone_attempts', 'red_zone_scores'], self.team),
            SplitIntParser(['red_zone_attempts_opp', 'red_zone_scores_opp'], self.team),
            None,
            PercentParser('field_goal_success_percent', self.team),
            PercentParser('field_goal_success_percent_opp', self.team),
            None,
            SplitIntParser(['field_goal_attempts', 'field_goals'], self.team),
            SplitIntParser(['field_goal_attempts_opp', 'field_goals_opp'], self.team),
            None,
            PercentParser('pat_kicking_success_percent', self.team),
            PercentParser('pat_kicking_success_percent_opp', self.team),
            None,
            SplitIntParser(['pat_kicking_attempts', 'pat_kicking_made'], self.team),
            SplitIntParser(['pat_kicking_attempts_opp', 'pat_kicking_made_opp'], self.team),
            None,
            PercentParser('two_point_conversion_success_percent', self.team),
            PercentParser('two_point_conversion_success_percent_opp', self.team),
            None,
            SplitIntParser(['two_point_conversion_attempts', 'two_point_conversions_made'], self.team),
            SplitIntParser(['two_point_conversion_attempts_opp', 'two_point_conversions_made_opp'], self.team),
        ]

    def handle_starttag(self, tag, attrs):
        pass#print(tag, attrs)

    def handle_endtag(self, tag):
        pass#print("Got end", tag)

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
