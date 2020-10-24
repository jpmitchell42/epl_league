import pdb, requests, json
from datetime import datetime
from epl_league_api.api.models import SoccerTeam, GameLine, Fixture
class ScrapeOdds:
  API_URL = 'https://api.the-odds-api.com/v3/odds'
  with open("secrets.json") as f:
    API_KEY = json.load(f)["the_odds_api_key"]

  @staticmethod
  def parse_odd(odds):
    pdb.set_trace()
    home_team = odds["home_team"]
    teams = odds["teams"]
    away_team = [team for team in odds["teams"] if team not in  [home_team]][0]
    away_team = teams - home_team
    available_odds = sorted(odds["sites"], key=lambda site: site["last_update"], reverse=True)
    most_recent_odds = available_odds[0]
    home_id = SoccerTeam.objects.all().filter(team_name=home_team)
    fixy = Fixture.objects.all().filter(home_team=home_team, away_team=away_team)

    start_time = datetime.fromtimestamp(odds["commence_time"])
    pdb.set_trace()



  @staticmethod
  def get_odds_from_api():
    response = requests.get(ScrapeOdds.API_URL, params={'api_key': ScrapeOdds.API_KEY,'sport': 'soccer_epl','region': 'uk','mkt': 'h2h'})
    data = json.loads(response.content)["data"]

    for o in data:
      ScrapeOdds.parse_odd(o)

def run():
    ScrapeOdds.get_odds_from_api()
    pdb.set_trace()

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
