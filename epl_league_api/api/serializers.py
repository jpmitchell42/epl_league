from django.contrib.auth.models import User, Group
from epl_league_api.api.models import SoccerTeam, Fixture, GameLine
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SoccerTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerTeam
        fields = ['id','team_name','city']

class GameLineSerialzer(serializers.ModelSerializer):
    class Meta:
        model = GameLine
        fields = '__all__'

class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields = '__all__'


# class Fixture(models.Model):
#   home_team = models.ForeignKey(SoccerTeam)
#   away_team = models.ForeignKey(SoccerTeam)
#   game_date = models.DateField()
#   gameweek = models.IntegerField()

# class GameLines(models.Model):
#   fixture = models.ForeignKey(Fixture)
#   home = models.IntegerField()
#   away = models.IntegerField()
#   tie = models.IntegerField()
#   pulled_on = models.DateTimeField()