from django.db import models

class SoccerTeam(models.Model):
  team_name = models.CharField(max_length=75)
  city = models.CharField(max_length=30)

  def __str__(self) -> str:
    return f"{self.team_name} {self.city}"