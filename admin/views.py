from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from jobs.models import Job

User = get_user_model()


def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.filter(is_staff=False).order_by("username")
    return render(request, "admin/user_list.html", {"users": users})


@user_passes_test(is_admin)
def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id, is_staff=False)
    if request.method == "POST":
        username = user.username
        user.delete()
        messages.success(request, f"Deleted user '{username}'.")
        return redirect("admin_panel:user_list")
    return render(request, "admin/user_confirm_delete.html", {"target_user": user})


@user_passes_test(is_admin)
def posting_list(request):
    postings = Job.objects.select_related("recruiter").order_by("-date")
    return render(request, "admin/posting_list.html", {"postings": postings})


@user_passes_test(is_admin)
def posting_delete(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == "POST":
        title = f"{job.title} at {job.company}"
        job.delete()
        messages.success(request, f"Deleted posting '{title}'.")
        return redirect("admin_panel:posting_list")
    return render(request, "admin/posting_confirm_delete.html", {"job": job})

# Create your views here.
