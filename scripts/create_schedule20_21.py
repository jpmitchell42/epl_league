from epl_league_api.api.models import SoccerTeam, Fixture
import csv, os, datetime, pdb
from collections import Set

SCHEDULE_CSV = os.path.join(os.getcwd(),"csvs","epl_20_21.csv")

def run():
    with open(SCHEDULE_CSV, "r") as fix_file:
      fixture_reader = csv.reader(fix_file)
      header = next(fixture_reader)
      teams = set()
      if header != None:
        # Iterate over each row after the header in the csv
        for row in fixture_reader:
            # row variable is a list that represents a row in csv
            gw = row[0]
            gamedate= row[1]
            away = row[2].replace(" FC","")
            home = row[4].replace(" FC","")
            away_team = SoccerTeam.objects.filter(team_name=away).first()
            home_team = SoccerTeam.objects.filter(team_name=home).first()
            datetime_object = datetime.datetime.strptime(gamedate, '%a %b %d %Y').date()
            new_fix = Fixture(home_team=home_team, away_team=away_team, game_date=datetime_object, gameweek=gw)
            new_fix.save()

      print(Fixture.objects.all().count())