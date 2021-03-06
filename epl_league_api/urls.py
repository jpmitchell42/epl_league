from django.urls import include, path
from rest_framework import routers
from epl_league_api.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'soccer_teams', views.SoccerTeamViewSet)
router.register(r'fixtures', views.FixtureViewSet)
router.register(r'game_lines', views.GameLineViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('gameweeks/', views.GameWeekApiView.as_view()),
    path('gameweeks/<int:week>/', views.GameWeekApiView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
