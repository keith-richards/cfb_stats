
# Almost all stats have 2 sides:
# Points Scored
# Points Scored by Opponent
#
# stats that end with _opp are the latter
class Team(object):
    def __init__(self):
        super().__init__()
        self.name = None
        
        self.points_per_game = None
        self.games = None
        self.points_scored = None
        self.first_downs = None
        self.rushing_first_downs = None
        self.passing_first_downs = None
        self.penalty_first_downs = None
        self.rushing_yards_per_attempt = None
        self.rushing_attempts = None
        self.rushing_yards = None
        self.rushing_tds = None
        self.passing_rating = None
        self.passing_yards = None
        self.passing_attempts = None
        self.passing_completions = None
        self.passing_interceptions = None
        self.passing_tds = None
        self.total_offense_yards_per_play = None
        self.total_offense_plays = None
        self.total_offense_yards = None
        self.punt_return_yards_per_return = None
        self.punt_return_yards = None
        self.punt_return_returns = None
        self.punt_return_tds = None
        self.kickoff_return_yards_per_return = None
        self.kickoff_return_yards = None
        self.kickoff_return_returns = None
        self.kickoff_return_tds = None
        self.punting_yards_per_punt = None
        self.punting_punts = None
        self.punting_yards = None
        self.interception_returns = None
        self.interception_yards = None
        self.interception_tds = None
        self.fumbles = None
        self.fumbles_lost = None
        self.penalties = None
        self.penalties_yards = None
        self.time_of_possession = None
        self.third_down_conversion_attempts = None
        self.third_down_conversions = None
        self.fourth_down_conversion_attempts = None
        self.fourth_down_conversions = None
        self.red_zone_attempts = None
        self.red_zone_scores = None
        self.field_goal_attempts = None
        self.field_goals = None
        self.pat_kicking_attempts = None
        self.pat_kicking_made = None
        self.two_point_conversion_attempts = None
        self.two_point_conversions_made = None

        self.points_per_game_opp = None
        self.points_scored_opp = None
        self.first_downs_opp = None
        self.rushing_first_downs_opp = None
        self.passing_first_downs_opp = None
        self.penalty_first_downs_opp = None
        self.rushing_yards_per_attempt_opp = None
        self.rushing_attempts_opp = None
        self.rushing_yards_opp = None
        self.rushing_tds_opp = None
        self.passing_rating_opp = None
        self.passing_yards_opp = None
        self.passing_attempts_opp = None
        self.passing_completions_opp = None
        self.passing_interceptions_opp = None
        self.passing_tds_opp = None
        self.total_offense_yards_per_play_opp = None
        self.total_offense_plays_opp = None
        self.total_offense_yards_opp = None
        self.punt_return_yards_per_return_opp = None
        self.punt_return_yards_opp = None
        self.punt_return_returns_opp = None
        self.punt_return_tds_opp = None
        self.kickoff_return_yards_per_return_opp = None
        self.kickoff_return_yards_opp = None
        self.kickoff_return_returns_opp = None
        self.kickoff_return_tds_opp = None
        self.punting_yards_per_punt_opp = None
        self.punting_punts_opp = None
        self.punting_yards_opp = None
        self.interception_returns_opp = None
        self.interception_yards_opp = None
        self.interception_tds_opp = None
        self.fumbles_opp = None
        self.fumbles_lost_opp = None
        self.penalties_opp = None
        self.penalties_yards_opp = None
        self.time_of_possession_opp = None
        self.third_down_conversion_attempts_opp = None
        self.third_down_conversions_opp = None
        self.fourth_down_conversion_attempts_opp = None
        self.fourth_down_conversions_opp = None
        self.red_zone_attempts_opp = None
        self.red_zone_scores_opp = None
        self.field_goal_attempts_opp = None
        self.field_goals_opp = None
        self.pat_kicking_attempts_opp = None
        self.pat_kicking_made_opp = None
        self.two_point_conversion_attempts_opp = None
        self.two_point_conversions_made_opp = None

