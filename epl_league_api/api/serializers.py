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
