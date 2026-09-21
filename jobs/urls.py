from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='jobs.index'), #implemented
    path('create/', views.create, name='jobs.create'), #implemented
    path('<int:id>/', views.show, name='jobs.show'), #implemented (test)
    path('<int:id>/edit/', views.edit, name='jobs.edit'), #still needs implementing
    # path('<int:id>/', views.apply, name='jobs.apply'), #still needs implementing

    #need one for job_detail (expanded /fullpage view)
    #need one for creating a job (as a recruiter)
    #need one for editing a job (as a recruiter)
    #need one for deleting a job (as a recruiter)
]