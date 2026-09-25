# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import (
    EducationFormSet, ExperienceFormSet, LinkFormSet, ProfileForm, SignUpForm,
)
from .models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect("job_seeker:index")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.role = form.cleaned_data["role"]
        profile.save()
        login(request, user)
        return redirect("job_seeker:index")
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        education = EducationFormSet(request.POST, instance=profile, prefix="education")
        experience = ExperienceFormSet(request.POST, instance=profile, prefix="experience")
        links = LinkFormSet(request.POST, instance=profile, prefix="links")

        # list, not generator, so every form gets validated and shows its errors
        if all([form.is_valid(), education.is_valid(), experience.is_valid(), links.is_valid()]):
            with transaction.atomic():
                form.save()
                education.save()
                experience.save()
                links.save()
            messages.success(request, "Profile saved.")
            return redirect("accounts:profile_edit")
    else:
        form = ProfileForm(instance=profile)
        education = EducationFormSet(instance=profile, prefix="education")
        experience = ExperienceFormSet(instance=profile, prefix="experience")
        links = LinkFormSet(instance=profile, prefix="links")

    return render(request, "accounts/profile_form.html", {
        "form": form,
        "education_formset": education,
        "experience_formset": experience,
        "link_formset": links,
    })