# projects/urls.py

from django.urls import path
from projects import views
from .views import portfolio

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('', portfolio, name='portfolio')
]
