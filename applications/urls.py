from django.urls import path
from . import views

urlpatterns = [
    path('<int:job_id>/apply/',views.apply,name='applications.apply'),
]