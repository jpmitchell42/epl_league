import pdb, requests, json, os, pytz
from datetime import datetime
from epl_league_api.api.models import SoccerTeam, GameLine, Fixture

TEAM_MAPPINGS = {
  "Brighton and Hove Albion" : "Brighton & Hove Albion"
}
class ScrapeOdds:
  API_URL = 'https://api.the-odds-api.com/v3/odds'
  API_KEY = os.environ.get("ODDS_API_KEY")

  @staticmethod
  def parse_odds(odds):
    home_team_raw = odds["home_team"]
    if home_team_raw in TEAM_MAPPINGS:
      home_team = TEAM_MAPPINGS[home_team_raw]
    else:
      home_team = home_team_raw
    
    raw_teams = odds["teams"]
    teams = [team if team not in TEAM_MAPPINGS else TEAM_MAPPINGS[team] for team in raw_teams]

    first_team_is_home_team = home_team == teams[0]
    away_team = teams[1] if first_team_is_home_team else teams[0]

    home_team = SoccerTeam.objects.all().filter(team_name=home_team).first()
    away_team = SoccerTeam.objects.all().filter(team_name=away_team).first()

    # TODO use date as well or we're fucked for future years
    possibilities = Fixture.objects.all().filter(home_team=home_team, away_team=away_team)
    if len(possibilities) != 1:
      print(f"cant find {home_team} vs {away_team}")
      raise RuntimeError
    game = possibilities.first()

    lines = odds["sites"]
    for site in lines:
      site_key = site["site_key"]
      last_update = datetime.fromtimestamp(site["last_update"]).replace(tzinfo=pytz.UTC)
      line = site["odds"]
      head_to_head = line.pop("h2h", None)
      
      if head_to_head:
        draw_int = head_to_head[2]
        
        if first_team_is_home_team:
          home_team_int = head_to_head[0]
          away_team_int = head_to_head[1]
        else:
          home_team_int = head_to_head[1]
          away_team_int = head_to_head[0]
        
        existing_line = GameLine.objects.filter(fixture=game, odds_source=site_key, pulled_on=last_update)

        if existing_line.count() == 1:
          existing_line.update(home=home_team_int, away=away_team_int, pulled_on=last_update)
        elif existing_line.count() > 1:
          print("raising runtime error because found multiple eligible gamelines")
          raise RuntimeError
        else:
          new_line = GameLine.objects.create(fixture=game, \
            odds_source=site_key, \
            pulled_on=last_update, \
            home=home_team_int, \
            away=away_team_int, \
            tie=draw_int
          )
          print(f"created newline: {new_line}")

  @staticmethod
  def get_odds_from_api():
    response = requests.get(ScrapeOdds.API_URL, params={'api_key': ScrapeOdds.API_KEY,'sport': 'soccer_epl','region': 'uk','mkt': 'h2h'})
    data = json.loads(response.content)["data"]
    for o in data:
      ScrapeOdds.parse_odds(o)

def run():
    ScrapeOdds.get_odds_from_api()

"""
apiKey   An API key is emailed when you sign up to a plan. See here for usage plans
sport   The sport key obtained from calling the /sports method. upcoming is always valid, returning any live games as well as the next 8 upcoming games across all sports
region   Determines which bookmakers are returned. Valid regions are au (Australia), uk (United Kingdom), eu (Europe) and us (United States)
mkt   Optional - Determines which odds market is returned. Defaults to h2h (head to head / moneyline). Valid markets are h2h, spreads (handicaps) and totals (over/under). spreads and totals odds are not always as comprehensive as h2h, so they do not count against the usage quota on paid plans.
Lay odds are automatically included with h2h results for relevant bookmakers (Betfair, Matchbook etc). These appear in the results under the h2h_lay key.
From July 2020, outrights are a valid market for sports with has_outrights: true. If the sport has outrights, set mkt=outrights. Lay odds for outrights (outrights_lay) will automatically be available for relevant exchanges. More info on outrights
dateFormat   Optional - Determines the format of timestamps in the response. Valid values are unix and iso (ISO 8601). Defaults to unix.
oddsFormat   Optional - Determines the format of odds in the response. Valid values are decimal and american. Defaults to decimal. When set to american, small discrepancies might exist for some bookmakers due to rounding errors.
"""
