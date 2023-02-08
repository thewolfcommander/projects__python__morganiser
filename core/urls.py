from django.urls import path

from .views import *

app_name = 'core'

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
]
