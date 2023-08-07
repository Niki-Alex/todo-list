from django.urls import path

from .views import (
    HomePage,
    ToggleAssignToTaskView,
)

urlpatterns = [
    path("", HomePage.as_view(), name="home-page"),
    path(
        "<int:pk>/toggle-assign/",
        ToggleAssignToTaskView.as_view(),
        name="toggle-task-assign"
    ),
]

app_name = "catalog"
