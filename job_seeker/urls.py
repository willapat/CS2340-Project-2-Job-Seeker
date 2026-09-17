from django.urls import path
from . import views

app_name = 'job_seeker'

urlpatterns = [
    path('', views.index, name='index'),
]