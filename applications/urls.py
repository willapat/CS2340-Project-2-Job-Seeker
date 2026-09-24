from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='applications.index'),
    path('<int:job_id>/apply/',views.apply,name='applications.apply'),

]