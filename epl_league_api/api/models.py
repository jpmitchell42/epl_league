from django.db import models

class SoccerTeam(models.Model):
  team_name = models.CharField(max_length=75)
  city = models.CharField(max_length=30)

  def __str__(self) -> str:
    return f"{self.team_name} {self.city}"

class Fixture(models.Model):
  home_team = models.ForeignKey(SoccerTeam ,on_delete=models.DO_NOTHING, related_name="home_team")
  away_team = models.ForeignKey(SoccerTeam, on_delete=models.DO_NOTHING, related_name="away_team")
  game_date = models.DateField()
  gameweek = models.IntegerField()

  def __str__(self) -> str:
    return f"{self.home_team} v {self.away_team}, {self.game_date}, gw:{self.gameweek}"

class GameLine(models.Model):
  fixture = models.ForeignKey(Fixture, on_delete=models.DO_NOTHING)
  home = models.IntegerField()
  away = models.IntegerField()
  tie = models.IntegerField()
  pulled_on = models.DateTimeField()
  odds_source = models.CharField(max_length=50, default="default")