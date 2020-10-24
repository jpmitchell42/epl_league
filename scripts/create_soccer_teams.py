from epl_league_api.api.models import SoccerTeam
import csv, os

TEAM_CSV = os.path.join(os.getcwd(),"csvs","teams.csv")

def run():
    teams = SoccerTeam.objects.all()
    with open(TEAM_CSV, "r") as club_file:
      club_reader = csv.reader(club_file)
      header = next(club_reader)
      if header != None:
        # Iterate over each row after the header in the csv
        for row in club_reader:
            # row variable is a list that represents a row in csv
            club_name = row[0]
            city = row[1]
            st = SoccerTeam.objects.get_or_create(team_name=club_name, city=city)
            print(st)
