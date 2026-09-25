from django.urls import path
from . import views

app_name = 'job_seeker'

urlpatterns = [
    path('', views.index, name='index'),
    # path('search/', views.job_search, name='job_search'), #we have now merged search and list together, so the url is now /jobs for both list and search
                                                                        #it is called job.index()
]