"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

from django.conf import settings
import os


codespace_name = os.environ.get('CODESPACE_NAME')
api_prefix = 'api/'

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_root(request):
    # Build the base URL using codespace name if available
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/{api_prefix}"
    else:
        # fallback to localhost for local dev
        base_url = f"http://localhost:8000/{api_prefix}"
    return JsonResponse({
        "users": base_url + "users/",
        "teams": base_url + "teams/",
        "activities": base_url + "activities/",
        "leaderboard": base_url + "leaderboard/",
        "workouts": base_url + "workouts/",
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_prefix}', api_root, name='api_root'),
    path(f'{api_prefix}', include(router.urls)),
]
