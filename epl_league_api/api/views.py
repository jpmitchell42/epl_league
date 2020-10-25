from epl_league_api.api.models import SoccerTeam
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from epl_league_api.api.serializers import UserSerializer, GroupSerializer, SoccerTeamSerializer, FixtureSerializer, GameLineSerialzer
from epl_league_api.api.models import SoccerTeam, Fixture, GameLine

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SoccerTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SoccerTeams to be viewd or edited
    """
    queryset = SoccerTeam.objects.all()
    serializer_class = SoccerTeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GameLineViewSet(viewsets.ModelViewSet):
    queryset = GameLine.objects.all()
    serializer_class = GameLineSerialzer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GameWeekApiView(APIView):
    def get(self, request, format=None, *args, **kwargs):
            week = kwargs.pop("week", None)
            if week:
                games = Fixture.objects.all().filter(gameweek=week)
                serializer = FixtureSerializer(games, many=True)
                return Response(serializer.data)
            else:
                gameweeks = sorted([ob["gameweek"] for ob in Fixture.objects.values('gameweek').distinct()])
                return Response({"weeks":gameweeks})

