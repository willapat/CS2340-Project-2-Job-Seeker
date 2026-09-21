from django.urls import path
from . import views

app_name = "admin_panel"

urlpatterns = [
    path("users/", views.user_list, name="user_list"),
    path("users/<int:user_id>/delete/", views.user_delete, name="user_delete"),
    path("postings/", views.posting_list, name="posting_list"),
    path("postings/<int:job_id>/delete/", views.posting_delete, name="posting_delete"),
]