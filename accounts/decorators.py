from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect

from .models import Profile

def job_seeker_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        profile = Profile.objects.filter(user=request.user).first()
        if profile is None or not profile.is_candidate:
            messages.error(request, "Only job seekers can use the cart.")
            return redirect("jobs.index")
        return view_func(request, *args, **kwargs)
    return wrapper