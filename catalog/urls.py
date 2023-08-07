from django.urls import path

from .views import (
    HomePage,
    # TopicListView,
    # TopicCreateView,
    # TopicUpdateView,
)

urlpatterns = [
    path("", HomePage.as_view(), name="home-page"),
]

app_name = "catalog"
